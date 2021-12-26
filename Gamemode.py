from cv2 import pointPolygonTest
import pyautogui
import keyboard
import os, ctypes
import time
import AutoAccept

try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if(is_admin == False):
    print('Please Run Script as Administrator')
    exit()

def __play__():
    p = pyautogui.locateOnScreen('./image/playbutton.png', confidence = 0.9)
    pyautogui.moveTo(p)
    pyautogui.doubleClick()
    time.sleep(1)
    return

def __confirm__():
    time.sleep(0.7)
    c = pyautogui.locateOnScreen('./image/confirm.png', confidence = 0.8)
    pyautogui.moveTo(c)
    pyautogui.doubleClick()
    time.sleep(0.7)
    gotit()
    AutoAccept.wait()

def __rift__():
    __play__()
    sr = pyautogui.locateOnScreen('./image/rift.png', confidence = 0.9)
    pyautogui.moveTo(sr)
    pyautogui.doubleClick()
    __confirm__()

def __aram__():
    __play__()
    ar = pyautogui.locateOnScreen('./image/aram.png', confidence = 0.9)
    pyautogui.moveTo(ar)
    pyautogui.doubleClick()
    __confirm__()

def __tft__():
    __play__()
    tf = pyautogui.locateOnScreen('./image/tft.png', confidence = 0.9)
    pyautogui.moveTo(tf)
    pyautogui.doubleClick()
    __confirm__()

def __coop__():
    __play__()
    cp = pyautogui.locateOnScreen('./image/coop.png', confidence = 0.9)
    pyautogui.moveTo(cp)
    pyautogui.doubleClick()
    __confirm__()

def __game__():
    os.system('cls')
    print("Choose The Gamemode You Want To Play")
    print()
    print('''1. Summoner's Rift
2. ARAM
3. Teamfight Tactics
4. Bots''')
    gm = 0
    while (gm == 0):
        if keyboard.is_pressed('1'):
            os.system('cls')
            __rift__()
        if keyboard.is_pressed('2'):
            os.system('cls')
            __aram__()
        if keyboard.is_pressed('3'):
            os.system('cls')
            __tft__()
        if keyboard.is_pressed('4'):
            os.system('cls')
            __coop__()

def gotit():
    time.sleep(1)
    gi = pyautogui.locateOnScreen('./image/gotit.png', confidence = 0.9)
    pyautogui.moveTo(gi)
    pyautogui.doubleClick()
    return

__game__()