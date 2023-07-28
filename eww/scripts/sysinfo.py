#!/usr/bin/env venv/bin/python

"""Gets general informations about the current UNIX system."""

import json
import subprocess
import os
import time
from dataclasses import dataclass
import psutil


@dataclass
class Sysinfo:
    """Describes the current state of the system."""

    cpu: int
    mem: int
    temp: int
    disk: int
    bat1: int
    bat2: int
    charging: bool


if __name__ == "__main__":
    while True:
        sysinfo = Sysinfo(
            cpu=int(round(psutil.cpu_percent(interval=1), 0)),
            mem=int(round(psutil.virtual_memory().percent, 0)),
            temp=int(round(psutil.sensors_temperatures()
                     ["coretemp"][0].current, 0)),
            disk=int(round(psutil.disk_usage("/").percent, 0)),
            bat1=0,
            bat2=0,
            charging=psutil.sensors_battery().power_plugged,
        )

        with open("/sys/class/power_supply/BAT1/capacity", "r", encoding="utf-8") as f:
            sysinfo.bat1 = int(f.read().strip("\n"))
        if int(sysinfo.bat1) <= 20 and not os.environ.get("BAT0_NOTIFIED"):
            subprocess.run(["notify-send", "WARNING",
                           "First battery low!"], check=True)
            os.environ["BAT0_NOTIFIED"] = "True"
        elif int(sysinfo.bat1) > 20 and os.environ.get("BAT0_NOTIFIED"):
            os.environ["BAT0_NOTIFIED"] = ""

        with open("/sys/class/power_supply/BAT0/capacity", "r", encoding="utf-8") as f:
            sysinfo.bat2 = int(f.read().strip("\n"))
        if int(sysinfo.bat2) <= 20 and not os.environ.get("BAT1_NOTIFIED"):
            subprocess.run(["notify-send", "WARNING",
                           "Second battery low!"], check=True)
            os.environ["BAT1_NOTIFIED"] = "True"
        elif int(sysinfo.bat2) > 20 and os.environ.get("BAT1_NOTIFIED"):
            os.environ["BAT1_NOTIFIED"] = ""

        print(json.dumps(sysinfo.__dict__), flush=True)
        time.sleep(1)
