import pyautogui as pg

def get_location(is_desktop, path, **kwargs):
    if 'region' in kwargs:
        if is_desktop:
            location = pg.locateCenterOnScreen(path, confidence=kwargs['confidence'], region=kwargs['region'])
        else:
            new_region = tuple(i * 2 for i in kwargs['region'])
            location = pg.locateCenterOnScreen(path, confidence=kwargs['confidence'], region=new_region)
    else:
        location = pg.locateCenterOnScreen(path, confidence=kwargs['confidence'])

    if location is not None:
        x, y = location 
        if is_desktop:
            return (x, y)
        else:
            return (x//2, y//2)

    else:
        print("찾을 수 없음")
        return None

def find_0(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/0.png'
    else:
        img_path = './images/number/laptop/0.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_2(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/2.png'
    else:
        img_path = './images/number/laptop/2.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_3(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/3.png'
    else:
        img_path = './images/number/laptop/3.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))
    
def find_4(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/4.png'
    else:
        img_path = './images/number/laptop/4.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_5(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/5.png'
    else:
        img_path = './images/number/laptop/5.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_6(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/6.png'
    else:
        img_path = './images/number/laptop/6.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_7(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/7.png'
    else:
        img_path = './images/number/laptop/7.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_8(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/8.png'
    else:
        img_path = './images/number/laptop/8.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

def find_9(is_desktop, region):
    if is_desktop:
        img_path = './images/number/desktop/9.png'
    else:
        img_path = './images/number/laptop/9.png'
    pg.click(get_location(is_desktop, img_path, confidence=0.99, region=region))

