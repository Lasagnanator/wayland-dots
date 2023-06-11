#!/usr/bin/env python3

"""Get informations about the current wifi network."""

from dataclasses import dataclass
import json
import textwrap as tw
import nmcli as nm


@dataclass
class Wifi:
    """Represents the data of a wifi connection."""

    name: str
    signal: int
    ip_addr: str


try:
    nmdev = nm.device()
    nmwifi = nm.device.wifi()
except Exception as e:  # pylint: disable=broad-exception-caught
    print(e)

active_device_list = [x for x in nmdev if x.state == "connected"]
active_wifi_list = [x for x in active_device_list if x.device_type == "wifi"]
active_wifi = active_wifi_list[0] if active_wifi_list else None
device_info = nm.device.show(active_wifi.device)
wifi_info_list = [
    x
    for x in nmwifi
    if x.ssid == (active_wifi.connection if active_wifi else "Disconnected")
]
wifi_info = wifi_info_list[0] if wifi_info_list else None
if active_wifi:
    wifi = Wifi(
        name="\n".join(tw.wrap(active_wifi.connection, 16, max_lines=2)),
        signal=wifi_info.signal,
        ip_addr=device_info["IP4.ADDRESS[1]"][
            0:device_info["IP4.ADDRESS[1]"].index("/")
        ],
    )

print(json.dumps(wifi.__dict__), flush=True)
