from pywinauto import application
from config import CHAT_ROOM_NAME


def send_message_to_chat(message):
    """
    채팅방에 메시지를 입력하고 전송하는 함수
    """
    try:
        # 채팅 애플리케이션에 연결
        app = application.Application(
            backend='uia').connect(title_re=CHAT_ROOM_NAME)

        # 채팅방 창 찾기
        dlg = app.window(title_re=CHAT_ROOM_NAME)

        # 메시지 입력 및 전송
        dlg['Document'].type_keys(message)
        dlg['Document'].type_keys('{ENTER}')  # 엔터 키로 메시지 전송
        print("메시지가 채팅창에 전송되었습니다:", message)

    except Exception as e:
        print("채팅창에 메시지를 보내는 중 오류 발생:", e)
