import pyperclip

user_input = input("left, top, right, bottom: ")
values = user_input.split()

left = int(values[0])
top = int(values[1])
right = int(values[2])
bottom = int(values[3])

width = right - left
height = bottom - top
print(f"({left}, {top}, {width}, {height})")
pyperclip.copy(f"({left}, {top}, {width}, {height})")
