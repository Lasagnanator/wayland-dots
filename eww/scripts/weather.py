#!/usr/bin/env venv/bin/python

"""Get weather informations from OpenWeatherMap."""

import json
from pyowm import OWM


with open('weather.json', 'r', -1, 'utf-8') as file:
    info = json.load(file)

owm = OWM(info['api_key'])
mgr = owm.weather_manager()
observation = mgr.weather_at_place(info['place'])

print(json.dumps(observation.weather.__dict__))
