import os

dir_path = './captchaCrack/imgs/test1/'

files = os.listdir(dir_path)
for file in files:
    old = os.path.join(dir_path, file)
    new = old + '.png'

    os.rename(old, new)