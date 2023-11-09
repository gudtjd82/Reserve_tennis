import pyautogui as pg

prev_pos = pg.position()
print(prev_pos)

while True:
    if pg.position() != prev_pos:
        prev_pos = pg.position()
        print(prev_pos)