#!/usr/bin/env venv/bin/python

"""Fetches info about pacman and AUR updates."""

import subprocess
import json
from dataclasses import dataclass


@dataclass
class Updates:
    """Represent the current number of updates of pacman and aur."""

    pacman: int
    aur: int


if __name__ == "__main__":
    updates = Updates(
        pacman=subprocess.run(['checkupdates'], capture_output=True, check=True).stdout.decode(
            'UTF-8').count('\n'),
        aur=subprocess.run(['rua', 'upgrade', '--printonly'],
                           capture_output=True, check=True).stdout.decode('UTF-8').count('\n'),
    )

    print(json.dumps(updates.__dict__), flush=True)
