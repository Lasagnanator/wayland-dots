#!/usr/bin/env python3

"""Get information on the current date and time."""

import datetime as dt
import json


def add_suffix(day: str) -> str:
    """Add the correct suffix to the number of day."""
    if day[1] == "1":
        day_suffix = f"{day}st"
    elif day[1] == "2":
        day_suffix = f"{day}nd"
    elif day[1] == "3":
        day_suffix = f"{day}rd"
    else:
        day_suffix = f"{day}th"
    day_suffix = day_suffix[1:] if day_suffix[0] == "0" else day_suffix
    return day_suffix
    # if it returns 0X instead of X, check for first character and trim


now = dt.datetime.now()
dt_info = {
    "weekday": now.strftime("%A").upper(),
    "day": add_suffix(now.strftime("%d").upper()),
    "month": now.strftime("%B").upper(),
    "year": now.strftime("%Y"),
    "time": now.strftime("%H:%M"),
}

print(json.dumps(dt_info), flush=True)
