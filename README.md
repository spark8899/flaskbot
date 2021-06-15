# flaskbot
from flask to send telegram

# init
```bash
cd /opt
python3 -m venv flask_bot
source /opt/flask_bot/bin/activate
pip install --upgrade pip
git clone https://github.com/spark8899/flaskbot.git && cd flaskbot
pip install -r requirements.txt
```


# add service
vim /etc/systemd/system/flaskbot.service
```
[Unit]
Description=flaskbot
After=network.target

[Service]
ExecStart=/opt/flask_bot/bin/gunicorn -b 0.0.0.0:8080 -w 4 --error-logfile - --access-logfile - main:app
WorkingDirectory=/opt/flask_bot/bots
StandardOutput=inherit
StandardError=inherit
Restart=always
User=chia
StandardOutput=file:/opt/flask_bot/bots/bot.log
StandardError=file:/opt/flask_bot/bots/bot.log

[Install]
WantedBy=multi-user.target
```

start flaskbot
```
systemctl daemon-reload
systemctl enable flaskbot
systemctl start flaskbot
```
# test api
```bash
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:28081/flaskbot -d '{"text": "testtttt"}'
```
