# 🚀 SBR Facebook Auto Messenger BOT

A fully mobile-compatible Facebook auto messaging bot built with Python, Flask, and Selenium — deployable on [Render](https://render.com) and usable directly from mobile.

---

## 🌟 Features

- 🔐 Login using Token or Email/Password
- 📤 Upload `msg.txt` file (messages to send)
- 🆔 Accept multiple UID targets (Inbox/Group)
- ⏱️ Custom delay (in seconds)
- 🔁 End-to-End Message Loop (E2E)
- 🧠 Auto Token Validation (via Graph API)
- 🛑 Start/Stop buttons with permanent STOP CODE: `1962020`
- 📜 Real-time Logs with timestamps and UID
- ✅ Render & Mobile Compatible

---

## 📁 File Structure

```
SBR_BOT/
├── app.py                 # Flask main app
├── Dockerfile             # Render deployment
├── requirements.txt       # Python dependencies
├── message_log.txt        # Logs of sent messages (auto-created)
├── static/
│   └── style.css          # Frontend CSS
├── templates/
│   └── index.html         # Web UI
└── utils/
    ├── sender.py          # Messaging logic (Selenium)
    ├── logger.py          # Logging logic
    ├── stop_flag.py       # Start/Stop logic
    └── validate_token.py  # Token checker
```

---

## 🛠️ Render Deployment Instructions

1. Go to [https://render.com](https://render.com) → Create new **Web Service**
2. Select **Deploy from GitHub** or Upload ZIP
3. In `Render Settings`:

   | Key              | Value              |
   |------------------|--------------------|
   | Runtime          | Docker             |
   | Port             | 10000              |
   | Root Directory   | `/` (root of SBR_BOT) |
   | Auto Deploy      | ✅ (optional)

4. Done. Bot will run at:  
   `https://your-app-name.onrender.com`

---

## 🧾 How to Use (via Web UI)

1. Paste one or more UIDs (Inbox or Group):
   ```
   10009866828472
   67669204872756
   ```

2. Upload `msg.txt` file — one message per line

3. Select login method:
   - **Token:** Paste long token string
   - **Email/Password:** Secure form input

4. Enter custom delay in seconds (e.g., `3`)

5. Click ✅ **Run Bot**

6. Live logs will appear below (with timestamps)

7. To stop the bot at any time, click ❌ **Stop Bot**

---

## 📌 Permanent Stop Code

The system will **immediately stop** if the user submits stop code:
```
1962020
```

---

## ❗ Important Notes

- Supports **E2E messages** (uses mbasic.facebook.com to avoid encryption block)
- Renders messages invisibly using **headless Chromium**
- Logs are auto-stored in `message_log.txt`

---

## 👑 Branding

All messages, logs, and UI use `SBR` label and colors.  
No external admin/owner tags – fully white-labeled for you.

---

## 💬 Need Help?

DM `@SBRRULEX` or open an issue.
