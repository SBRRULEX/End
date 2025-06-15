# app.py
from flask import Flask, render_template, request, redirect, jsonify
from utils.logger import log_message
from utils.sender import start_bot
from utils.stop_flag import set_stop_flag, get_stop_flag
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    uids = request.form.get('uids').strip().splitlines()
    delay = int(request.form.get('delay'))
    login_method = request.form.get('login_method')
    stop_code = request.form.get('stop_code')

    # Save uploaded msg.txt
    msg_file = request.files.get('msg_file')
    msg_path = os.path.join(UPLOAD_FOLDER, 'msg.txt')
    msg_file.save(msg_path)

    credentials = {}
    if login_method == 'token':
        credentials['token'] = request.form.get('token')
    else:
        credentials['email'] = request.form.get('email')
        credentials['password'] = request.form.get('password')

    # Reset stop flag before starting
    set_stop_flag(False)

    # Start bot in background
    import threading
    threading.Thread(
        target=start_bot,
        args=(uids, msg_path, delay, login_method, credentials)
    ).start()

    return jsonify({"status": "Bot Started"})

@app.route('/stop', methods=['POST'])
def stop():
    user_code = request.form.get('code')
    if user_code == "1962020":
        set_stop_flag(True)
        return jsonify({"status": "Bot stopped successfully."})
    else:
        return jsonify({"error": "Invalid stop code."}), 401

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"stopped": get_stop_flag()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
