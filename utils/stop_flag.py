# utils/stop_flag.py

import json
import os

FLAG_FILE = 'stop_flag.json'

def set_stop_flag(value: bool):
    with open(FLAG_FILE, 'w') as f:
        json.dump({'stop': value}, f)

def get_stop_flag():
    if not os.path.exists(FLAG_FILE):
        return False
    with open(FLAG_FILE, 'r') as f:
        data = json.load(f)
        return data.get('stop', False)
