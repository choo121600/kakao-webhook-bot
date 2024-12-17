from flask import Flask
from server.webhook_hander import handle_webhook

app = Flask(__name__)

# 웹훅 엔드포인트 설정


@app.route('/webhook', methods=['POST'])
def webhook():
    return handle_webhook()


if __name__ == '__main__':
    # Flask 서버 실행
    app.run(host='0.0.0.0', port=5000, debug=True)
