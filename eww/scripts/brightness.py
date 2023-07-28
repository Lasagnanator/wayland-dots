#!/usr/bin/env venv/bin/python

"""Get brightness in real time."""

from typing import Callable
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class WatchFile(FileSystemEventHandler):
    """Watchfile class for checking when a file changes."""

    def __init__(self, path: str, filename: str, callback: Callable) -> None:
        """Create an instance of the class."""
        self.filename = filename
        self.callback = callback
        self.observer = Observer()
        self.observer.schedule(self, path, recursive=False)
        self.observer.start()
        self.observer.join()

    def on_modified(self, event):
        """Exec the callback function when the state of the file changes."""
        if not event.is_directory and event.src_path.endswith(self.filename):
            self.callback()


if __name__ == "__main__":

    with open("/sys/class/backlight/intel_backlight/max_brightness", "r", encoding="utf-8") as file:
        max_brightness = file.read().strip("\n")

    def get_brightness_from_file() -> None:
        """Get brightness from the system file."""
        with open("/sys/class/backlight/intel_backlight/brightness", "r", encoding="utf-8") as file:  # pylint: disable=redefined-outer-name
            raw_brightness = file.read().strip("\n")
        brightness = int(
            round(((int(raw_brightness) / int(max_brightness)) * 100), 0))
        print(brightness, flush=True)

    get_brightness_from_file()
    WatchFile("/sys/class/backlight/intel_backlight/", "brightness", get_brightness_from_file)
