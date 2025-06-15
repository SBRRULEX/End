# utils/logger.py

import os
from datetime import datetime

LOG_FILE = 'message_log.txt'

def log_message(uid, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] SBR SENT to UID: {uid} → {message.strip()}\n"

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)
