#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

from typing import List
from ui.icon import Icon

def scan_for_apps() -> List[str]:
    apps = []

    for directory in os.listdir(os.environ["APP"]):
        if os.path.isfile(os.path.join(os.path.join(os.environ["APP"], directory), "manifest.json")):
            apps.append(os.path.join(os.environ["APP"], directory))
    
    return apps

def get_app_icons(app_dir: List[str]) -> List[Icon]:
    icons = []

    for directory in app_dir:
        with open(os.path.join(directory, "manifest.json"), 'r') as config:
            jsonData = json.load(config)
            icons.append(Icon(directory, os.path.join(directory, jsonData["icon"])))
   
    return icons
            