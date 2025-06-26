from flask import Flask
from server.webhook_handler import handle_webhook

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    return handle_webhook()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
