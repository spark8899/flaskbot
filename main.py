#!/opt/flask_bot/bin/python3
from flask import Flask, request, jsonify
import logging, requests
from logging.handlers import RotatingFileHandler
from logging import Formatter

app = Flask(__name__)
telbot_id = 'bot111111:aaaaaaaa-bbbbbbb'
chia_id = '-000000'
log_path = '/opt/flask_bot/bots/bot.log'

@app.route('/')
def home():
    app.logger.warning("client: %s, path: /" % request.remote_addr)
    return "<p>Hello, World!</p>"

@app.route('/flaskbot', methods=["POST"])
def chia():
    data = request.get_json()
    app.logger.warning("client: %s, data: %s" % (request.remote_addr, data))
    url = "https://api.telegram.org/%s/sendMessage" % telbot_id
    if "text" in data:
        content = {"chat_id": chat_id, "text": data['text'], "parse_mode": "markdown"}
        app.logger.warning("content: %s" % content)
        req = requests.post(url, content)
        #print(req.json())
    return jsonify(data)

if __name__ == '__main__':
    log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'
    handler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=5)
    handler.setFormatter(Formatter(log_format))
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=8080)
