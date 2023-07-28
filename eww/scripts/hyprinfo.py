#!/usr/bin/env venv/bin/python

"""Information about the state of Hyprland."""

from dataclasses import dataclass
from typing import List
import os
import socket
import subprocess
import json
import re


@dataclass
class Monitor:
    """Id, name and workspace of every connected monitor."""

    monitor_id: int
    name: str
    active_workspace: int


@dataclass
class Workspace:
    """Id and number of windows in every workspace."""

    workspace_id: int
    windows: int


@dataclass
class Window:
    """Class and tile of current window."""

    classname: str
    title: str


@dataclass
class Hyprinfo:
    """Current state of monitors, workspaces and current window in Hyprland."""

    monitors: List[Monitor]
    workspaces: List[Workspace]
    window: Window

    def to_json(self):
        """Export the class in JSON."""
        json: dict = {  # pylint: disable=redefined-outer-name
            "monitors": [x.__dict__ for x in self.monitors],
            "workspaces": [x.__dict__ for x in self.workspaces],
            "window": self.window.__dict__,
        }
        return json


def title_filter(window_info: dict) -> str:
    """Filter the name of the current window."""
    if bool(re.search("(?i)firefox", window_info["class"])):
        window_name = "firefox"
    elif bool(re.search("(?i)notion", window_info["class"])):
        window_name = "notion"
    elif bool(re.search("(?i)discord", window_info["class"])):
        window_name = "discord"
    else:
        window_name = window_info["title"]
    return window_name


def hyprland_status():
    """Fetch and print the current state of Hyprland in JSON."""
    hyprinfo: Hyprinfo = Hyprinfo(
        monitors=[], workspaces=[], window=Window("None", "None")
    )
    raw_data = json.loads(
        subprocess.run(["hyprctl", "monitors", "-j"],
                       capture_output=True, check=True).stdout
    )
    for i in range(0, 4):
        monitor = [x for x in raw_data if x["id"] == i]
        hyprinfo.monitors.append(
            Monitor(
                monitor_id=i,
                name=monitor[0]["name"] if monitor else "disconnected",
                active_workspace=int(monitor[0]["activeWorkspace"]["id"])
                if monitor
                else 1,
            )
        )
    raw_data = json.loads(
        subprocess.run(["hyprctl", "workspaces", "-j"],
                       capture_output=True, check=True).stdout
    )
    for i in range(1, 10):
        workspace = [x for x in raw_data if x["id"] == i]
        hyprinfo.workspaces.append(
            Workspace(workspace_id=i, windows=int(
                workspace[0]["windows"]) if workspace else 0)
        )
    raw_data = json.loads(
        subprocess.run(["hyprctl", "activewindow", "-j"],
                       capture_output=True, check=True).stdout
    )
    hyprinfo.window = Window(
        classname=raw_data["class"] if raw_data else "Null",
        title=title_filter(raw_data).capitalize() if raw_data else "Null",
    )
    print(json.dumps(hyprinfo.to_json()), flush=True)


if __name__ == "__main__":
    hyprland_status()
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(
            f'/tmp/hypr/{os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")}/.socket2.sock')
        while True:
            output = sock.recv(4096).decode("utf-8")
            if (
                output.split("\n")[0][0:14] == "activewindow>>"
                or output.split("\n")[0][0:11] == "workspace>>"
                or output.split("\n")[0][0:12] == "focusedmon>>"
            ):
                hyprland_status()
