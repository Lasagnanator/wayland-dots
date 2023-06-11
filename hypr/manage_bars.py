#!/usr/bin/env python

"""Open and close EWW bars based on connected monitors."""

import os
import socket
import subprocess
import json
import re


def manage_bars():
    """Check which monitor is connected and open the corresponding bar."""
    monitors = json.loads(subprocess.run(
        ['hyprctl', 'monitors', '-j'], capture_output=True, check=True).stdout)
    all_bars = subprocess.run(
        ['eww', 'windows'], capture_output=True, check=True).stdout.decode('utf-8')
    print(all_bars)
    open_cmd = ['eww', 'open-many']
    for idx, _ in enumerate(monitors):
        regex = re.compile(rf'\*bar{idx}')
        open_bars = regex.findall(all_bars)
        if not open_bars:
            open_cmd.append(f'bar{idx}')
    subprocess.run(open_cmd, check=True)


if __name__ == "__main__":
    manage_bars()
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(
            f'/tmp/hypr/{os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")}/.socket2.sock')
        while True:
            output = sock.recv(4096).decode('utf-8')
            if output.split('\n')[0][0:16] == 'monitorremoved>>' or output.split('\n')[0][0:14] == 'monitoradded>>':  # pylint: disable=line-too-long
                manage_bars()
