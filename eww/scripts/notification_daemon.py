#!/usr/bin/env venv/bin/python

"""Notification daemon based on DBUS and sockets."""

import os
import datetime
import json
import socket
import threading
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

NOTIF_CACHE_PATH = Path('/tmp/notification_cache')
CURRENT_SOCK = Path(f'{NOTIF_CACHE_PATH}/current.sock')
HISTORY_SOCK = Path(f'{NOTIF_CACHE_PATH}/history.sock')
IMG_CACHE = Path(f'{NOTIF_CACHE_PATH}/img')

def recv_notif():
    """Read DBUS to recieve notifications."""

def cache_image():
    """Cache images from stupid Electron services."""

def send_current():
    """Write to a socket the current notification."""

def send_history():
    """Write to a socket all previous notifications."""

def get_current():
    """Get current notifications."""

def get_history():
    """Get old notifications."""

if __name__ == "__main__":
    pass
