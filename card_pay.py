import pyautogui as pg
import time
from get_location import *

def card_pay_desktop():
    # 전체동의
    pg.click(1400, 566)

    # 신한카드 선택
    pg.click(1288, 717)

    # 다음
    pg.click(1577, 1049)
    time.sleep(2)

    # 다른결제 선택
    pg.click(1376, 670)
    time.sleep(1)

    # 일반 결제 선택
    pg.click(1168, 826)
    time.sleep(1)

    # 카드번호 입력창 클릭
    pg.click(1208, 737)
    time.sleep(0.3)

    # 카드번호 입력 0 2 3 4 5 6 7 8 9
    pg.typewrite('5')
    pg.typewrite('4')
    pg.typewrite('2')
    pg.typewrite('8')

    time.sleep(0.3)
    find_7(True, (1206, 736, 271, 184))
    time.sleep(0.3)
    find_9(True, (1206, 736, 271, 184))
    time.sleep(0.3)
    find_6(True, (1206, 736, 271, 184))
    time.sleep(0.3)
    find_7(True, (1206, 736, 271, 184))

    time.sleep(2)
    find_0(True, (1206, 736, 271, 184))
    time.sleep(0.3)
    find_3(True, (1206, 736, 271, 184))
    time.sleep(0.3)
    find_5(True, (1370, 779, 106, 133))
    time.sleep(0.3)
    find_0(True, (1206, 736, 271, 184))
    time.sleep(0.3)

    time.sleep(0.5)
    pg.typewrite('3')
    pg.typewrite('4')
    pg.typewrite('9')
    pg.typewrite('6')
    time.sleep(0.3)

    # cvc번호 입력창 클링
    pg.click(1206, 787)
    time.sleep(0.2)

    # cvc번호 입력
    find_6(True, (1200, 836, 215, 113))
    time.sleep(0.3)
    find_4(True, (1200, 836, 215, 113))
    time.sleep(0.3)
    find_0(True, (1200, 836, 215, 113))
    time.sleep(0.3)
    pg.click(1350, 928)

    # 다음 클릭
    pg.click(1373, 973)
    time.sleep(1)


    # 입력창 클릭
    pg.click(1193, 835)
    time.sleep(1)

    # 비밀번호 입력
    pg.click(get_location(True, './images/password/d.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/y.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/d.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/w.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/n.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/1.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/1.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/2.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/4.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(1141, 795)
    time.sleep(0.3)
    pg.click(get_location(True, './images/password/$.png', confidence=0.99, region=(1044, 631, 462, 220)))
    time.sleep(0.3)
    pg.click(1452, 796)
    pg.click(1376, 974)
    time.sleep(2)
    pg.click(1578, 1049)

def card_pay_laptop():
    # 전체동의
    pg.click(955, 373)

    # 신한카드 선택
    pg.click(838, 522)

    # 다음
    pg.click(1135, 858)
    time.sleep(2)

    # 다른결제 선택
    pg.click(932, 478)
    time.sleep(1)

    # 일반 결제 선택
    pg.click(807, 631)
    time.sleep(1)

    # 카드번호 입력창 클릭
    pg.click(768, 542)
    time.sleep(0.3)

    # 카드번호 입력 0 2 3 4 5 6 7 8 9
    pg.typewrite('5')
    pg.typewrite('4')
    pg.typewrite('2')
    pg.typewrite('8')

    time.sleep(0.3)
    find_7(False, (756, 537, 294, 204))
    time.sleep(0.3)
    find_9(False, (756, 537, 294, 204))
    time.sleep(0.3)
    find_6(False, (756, 537, 294, 204))
    time.sleep(0.3)
    find_7(False, (756, 537, 294, 204))

    time.sleep(2)
    find_0(False, (756, 537, 294, 204))
    time.sleep(0.3)
    find_3(False, (756, 537, 294, 204))
    time.sleep(0.3)
    find_5(False, (934, 589, 86, 91))
    time.sleep(0.3)
    find_0(False, (756, 537, 294, 204))
    time.sleep(0.3)

    time.sleep(0.5)
    pg.typewrite('3')
    pg.typewrite('4')
    pg.typewrite('9')
    pg.typewrite('6')
    time.sleep(0.3)

    # cvc번호 입력창 클링
    pg.click(763, 592)
    time.sleep(0.2)

    # cvc번호 입력
    find_6(False, (720, 594, 270, 175))
    time.sleep(0.3)
    find_4(False, (720, 594, 270, 175))
    time.sleep(0.3)
    find_0(False, (720, 594, 270, 175))
    time.sleep(0.3)
    pg.click(904, 734)

    # 다음 클릭
    pg.click(934, 781)
    time.sleep(2)


    # 입력창 클릭
    pg.click(777, 639)
    time.sleep(1)

    # 비밀번호 입력
    pg.click(get_location(False, './images/password/laptop/d.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/y.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/d.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/w.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/n.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/1.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/1.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/2.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/4.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(700, 599)
    time.sleep(0.3)
    pg.click(get_location(False, './images/password/laptop/$.png', confidence=0.99, region=(614, 452, 440, 187)))
    time.sleep(0.3)
    pg.click(1006, 603)
    pg.click(930, 780)
    time.sleep(2)
    pg.click(1138, 858)

if __name__ == "__main__":
    time.sleep(3)
    card_pay_laptop()