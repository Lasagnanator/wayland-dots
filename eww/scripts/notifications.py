#!/usr/bin/env venv/bin/python

"""Manages notifications from DBUS."""

import os
import shutil
import datetime
import json
from pathlib import Path
from dataclasses import dataclass
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import GLib, GdkPixbuf


@dataclass
class Notification:
    """Represents a notification read from the system."""

    ntf_id: int
    title: str
    body: str
    icon: str
    app: str
    urgency: int


CACHE_PATH = Path('/tmp/notification_cache')
ntf_cache: list[Notification] = []


def get_thumbnail(path, message):
    """Save the thumbnail if bytes are sent."""
    icon_data = message[6].get('image-data')
    if icon_data:
        GdkPixbuf.Pixbuf.new_from_bytes(
            width=icon_data[0],
            height=icon_data[1],
            has_alpha=icon_data[3],
            data=GLib.Bytes(bytes(list(icon_data[6]))),
            colorspace=GdkPixbuf.Colorspace.RGB,
            rowstride=icon_data[2],
            bits_per_sample=icon_data[4],
        ).savev(bytes(path), 'png')
        return True
    return False


def get_notif(_ , message_raw):
    """Get notifications from the system."""
    if not isinstance(message_raw, dbus.lowlevel.MethodCallMessage):
        return
    message = message_raw.get_args_list()
    ntf_id = int(datetime.datetime.now().timestamp() * 1e6)
    thumbnail_path = Path(f'{CACHE_PATH}/{ntf_id}.png')
    thumbnail_status = get_thumbnail(thumbnail_path, message)
    notification = Notification(
        ntf_id=int(ntf_id),
        title=str(message[3]),
        body=str(message[4]),
        icon=str(thumbnail_path) if thumbnail_status else '',
        app=str(message[0]),
        urgency=int(message[6].get('urgency'))
    )
    # print(json.dumps(notification.__dict__), flush=True)
    while len(ntf_cache) >= 20:
        os.remove(ntf_cache[0].icon)
        ntf_cache.pop(0)
    ntf_cache.append(notification)
    # with open(f'{CACHE_PATH}/cache.json', 'w', encoding='utf-8') as file:
    #     json.dump([item.__dict__ for item in ntf_cache],
    #               file)
    ntf_complete = {
            'last': notification.__dict__,
            'cache': [item.__dict__ for item in ntf_cache]
            }
    print(json.dumps(ntf_complete), flush=True)


if __name__ == "__main__":
    shutil.rmtree(CACHE_PATH, ignore_errors=True)
    os.makedirs(CACHE_PATH)
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    bus.add_match_string_non_blocking("eavesdrop=true, \
                                       interface='org.freedesktop.Notifications', \
                                       member='Notify'")
    bus.add_message_filter(get_notif)
    loop = GLib.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt:
        bus.close()
