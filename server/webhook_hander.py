from flask import request, jsonify
import json
from chat.chat_sender import send_message_to_chat


def handle_webhook():
    """
    웹훅 데이터를 처리하고 채팅방에 메시지를 전송하는 함수
    """
    try:
        data = request.json

        if "embeds" in data and len(data["embeds"]) > 0:
            embed = data["embeds"][0]  # 첫 번째 embed만 처리 (필요시 수정 가능)

            author_name = embed.get('author', {}).get('name', 'Unknown Author')
            title = embed.get('title', 'No Title')
            url = embed.get('url', '')
            description = embed.get('description', '')

            max_description_length = 100
            if len(description) > max_description_length:
                description = description[:max_description_length] + "..."

            message = f"{title}\n\n" \
                f"{description}\n\n"\
                f"{url}" 


            print("수신된 embed 메시지:", message)
            send_message_to_chat(message)
        else:
            print("webhook에 데이터가 없습니다. 메시지를 전송하지 않습니다.")

        return jsonify({"message": "웹훅 데이터 수신 및 처리 완료"}), 200

    except Exception as e:
        print("웹훅 처리 중 오류 발생:")
        return jsonify({
            "error": "서버 오류",
            "exception": str(e)
        }), 500
