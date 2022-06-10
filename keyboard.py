import time

import keyboard
import pyperclip
li=[]
def fek():
    print("ctrl+alt+j was pressed")
n=0
while True:
    if keyboard.is_pressed('ctrl+alt+j'):
        fek()
    if keyboard.is_pressed('ctrl+c'):
        li.append(pyperclip.paste())
        time.sleep(0.1)
    if keyboard.is_pressed('ctrl+o'):
        pyperclip.copy(li[-n])
        print(pyperclip.paste())
        time.sleep(0.1)
        n=n+1
        if n==(len(li)-1):
            n=0
    if keyboard.is_pressed('alt+o'):
        pyperclip.copy(li[-n])
        print(pyperclip.paste())
        time.sleep(0.1)
        n=n-1
        if n==0:
            n=(len(li)-1)
        if n<(-(len(li)-1)):
            n=0
    if keyboard.is_pressed('alt+l'):
        print(li)
        print(n)
        print(len(li))
        time.sleep(0.1)
    for c in li:
        if c=='':
            li.remove(c)