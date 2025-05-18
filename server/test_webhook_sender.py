from flask import jsonify
import json
from chat.chat_sender import send_message_to_chat


def test_handle_webhook_with_example_file():
    """
    example_webhook.json 파일을 읽고 handle_webhook 함수의 로직을 모방하여 메시지를 전송하는 테스트 함수
    """
    try:
        with open('../example_webhook.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        if "embeds" in data and len(data["embeds"]) > 0:
            embed = data["embeds"][0]  # 첫 번째 embed만 처리

            author_name = embed.get('author', {}).get('name', 'Unknown Author')
            title = embed.get('title', 'No Title')
            url = embed.get('url', '')
            description = embed.get('description', '')

            max_description_length = 100
            if len(description) > max_description_length:
                description = description[:max_description_length] + "..."

            message = f"{title}\n\n" \
					f"{description}\n\n" \
					f"{url}"

            print("테스트용 embed 메시지:", message)
            send_message_to_chat(message)
        else:
            print("example_webhook.json에 유효한 embed 데이터가 없습니다.")

    except Exception as e:
        print("example_webhook.json 테스트 중 오류 발생:", e)
        return jsonify({
            "error": "서버 오류",
            "exception": str(e)
        }), 500
