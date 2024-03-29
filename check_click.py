from pynput.mouse import Listener, Button
import pyautogui

def on_click(x, y, button, pressed):
    # 마우스 왼쪽 버튼이 눌렸는지 확인하고, 눌렸다면 위치를 출력한 후 리스너 종료
    if button == Button.left and pressed:
        print(f"Left click detected at position: ({x}, {y})")
        # 클릭 위치를 전역 변수에 저장
        global click_position
        click_position = (int(x), int(y))
        # 리스너를 종료하기 위해 False 반환
        return False

def get_click_position():
    print("Waiting for one left mouse click...")
    # 전역 변수 초기화
    global click_position
    click_position = None
    # 마우스 클릭 리스너 시작
    with Listener(on_click=on_click) as listener:
        listener.join()
    # 저장된 클릭 위치 반환
    return click_position

# 함수 사용 예시
# position = get_click_position()
# print(f"Mouse clicked at: {position}")
