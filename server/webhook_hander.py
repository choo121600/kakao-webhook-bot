from flask import request, jsonify
import json
from config import TEXT_FILE
from chat.chat_sender import send_message_to_chat


def handle_webhook():
    """
    웹훅 데이터를 처리하고 채팅방에 메시지를 전송하는 함수
    """
    try:
        data = request.json

        # 데이터를 파일에 저장
        with open(TEXT_FILE, "a", encoding="utf-8") as file:
            json_data = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(json_data + "\n\n")
        print("웹훅 데이터가 저장되었습니다!")

        if "content" in data:
            message = data["content"]
            print("수신된 메시지:", message)

            # 채팅방에 메시지 전송
            send_message_to_chat(message)
        else:
            print("content가 없습니다. 메시지를 전송하지 않습니다.")

        return jsonify({"message": "웹훅 데이터 수신 및 처리 완료"}), 200

    except Exception as e:
        print("웹훅 처리 중 오류 발생:", e)
        return jsonify({"error": "서버 오류"}), 500
