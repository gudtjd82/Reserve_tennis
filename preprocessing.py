import pyautogui as pg
import os
import time
from pynput.mouse import Listener
from PIL import Image
import matplotlib.pyplot as plt

def on_click(x, y, button, pressed):
    if pressed:
        print("clicked!")
        return False

def captureCaptcha(dirName, captcha_region):
    dir_path = './captchaCrack/imgs/' + dirName + '/'

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    files = os.listdir(dir_path)
    
    # .png 파일만 골라내기
    png_files = [file for file in files if file.endswith('.png')]
    
    # 파일 이름에서 숫자 부분만 가져와서 정수로 변환, 그 중 최댓값 찾기
    max_num = max(int(file.replace('.png', '')) for file in png_files) if png_files else 0
    
    # 다음 숫자 계산
    img_num = max_num + 1

    img = pg.screenshot(region=captcha_region)
    final_path = dir_path + str(img_num) + '.png'
    img.save(final_path)

    return final_path

def makeSamples(path, n, start_num, captcha_region):
    ms_x, ms_y = pg.position()
    print(f"마우스 위치 확인!: ({ms_x}, {ms_y})")
    for i in range(n):
        pg.click(ms_x, ms_y)
        img = pg.screenshot(region=captcha_region)
        final_path = path + 'raw_' + str(i+start_num) + '.png'
        img.save(final_path)

def make_label(path):
    files = os.listdir(dir_path)

    # raw_00.png 파일만 골라내기
    png_files = [file for file in files if file.startswith('raw_') and file.endswith('.png')]

    plt.ion()

    i = 0;
    for png in png_files:
        image_path = os.path.join(dir_path, png)
        
        # 이미지 파일 열기
        img = Image.open(image_path)
        
        # 이미지 파일 보여주기
        plt.imshow(img)
        plt.show()
        plt.pause(0.001)
        
        new_name = input(f"Enter new name for {png}: ")
        new_path = os.path.join(dir_path, 'labeled/')
        new_path = os.path.join(new_path, new_name) + '.png'
        
        os.rename(image_path, new_path)
        i += 1
        remain_files = len(png_files)-i
        print(f"남은 파일 수: {remain_files}")

        plt.clf()

if __name__ == "__main__":
    sel = input("1. sample 캡쳐 | 2. sample 이름 생성: ")

    # sample 생성
    if sel == '1':
        n = input("몇 장을 캡쳐할까요? : ")
        dirName = input("저장할 폴더 명을 입력하세요 : ")

        dir_path = './captchaCrack/imgs/' + dirName + '/'
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        files = os.listdir(dir_path)
        
        png_files = [file for file in files if file.startswith('raw_') and file.endswith('.png')]
        # 파일 이름에서 숫자 부분만 가져와서 정수로 변환, 그 중 최댓값 찾기
        max_num = max(int(file.replace('raw_', '').replace('.png', '')) for file in png_files) if png_files else 0
        # 다음 숫자 계산
        next_num = max_num + 1

        with Listener(on_click=on_click) as listener:
            listener.join()

        captcha_region = (259, 542, 236, 88)
        time.sleep(2)
        makeSamples(dir_path, int(n), next_num, captcha_region)

        print("Completed!")
    
    # sample label 생성
    elif sel == '2':
        dirName = input("폴더 명을 입력하세요 : ")
        dir_path = './captchaCrack/imgs/' + dirName + '/'
        make_label(dir_path)