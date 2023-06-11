#!/usr/bin/env python3

"""Get the current volume in real time."""

import subprocess
import pulsectl


def get_volume():
    """Get the current volume from pamixer."""
    mute = subprocess.run(['pamixer', '--get-mute'],
                          capture_output=True, check=True).stdout.decode("utf-8").rstrip()
    if mute == 'true':
        print('MUTE', flush=True)
    else:
        volume = subprocess.run(['pamixer', '--get-volume'],
                                capture_output=True, check=True).stdout.decode("utf-8").rstrip()
        print(volume, flush=True)


def stop_loop(_):
    """Pause the current listening loop to fetch the volume."""
    raise pulsectl.PulseLoopStop


with pulsectl.Pulse('event-printer') as pulse:
    get_volume()
    while True:
        pulse.event_mask_set('all')
        pulse.event_callback_set(stop_loop)
        pulse.event_listen()
        get_volume()
