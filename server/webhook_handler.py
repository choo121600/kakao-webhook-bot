from flask import request, jsonify
import json
import re
from config import TEXT_FILE

from chat.chat_sender import send_message_to_chat


def clean_markdown(description: str) -> str:
    """
    마크다운 링크와 불완전한 마크다운 링크를 제거하는 함수
    """
    description = re.sub(r'\[[^\]]*\]\([^)]+\)', '', description)

    description = re.sub(r'\[[^\]]*\]\([^\)]*$', '', description)
    description = re.sub(r'\[[^\]]*$', '', description)

    return description


def handle_webhook():
    """
    웹훅 데이터를 처리하고 채팅방에 메시지를 전송하는 함수
    """
    try:
        data = request.json
        with open(TEXT_FILE, "a", encoding="utf-8") as file:
            json_data = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(json_data + "\n\n")
        print("웹훅 데이터가 저장되었습니다!")

        if "embeds" in data and len(data["embeds"]) > 0:
            embed = data["embeds"][0]  # 첫 번째 embed만 처리

            author_name = embed.get('author', {}).get('name', 'Unknown Author')
            title = embed.get('title', 'No Title')
            url = embed.get('url', '')
            description = embed.get('description', '')

            description = clean_markdown(description)

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
        print("웹훅 처리 중 오류 발생:", e)
        return jsonify({
            "error": "서버 오류",
            "exception": str(e)
        }), 500 