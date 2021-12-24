import pyautogui
import keyboard
import os, ctypes

try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if(is_admin == False):
    print('Please Run Script as Administrator')
    exit()

def find():
    os.system('cls')
    f = pyautogui.locateOnScreen('./image/find.png', confidence = 0.8)
    pyautogui.moveTo(f)
    pyautogui.doubleClick()
    accept()

def accept():
    a = None
    print ('Waiting For Queue')
    print ()
    print ('Press Escape To Cancel Queue')
    while(a == None):
        a = pyautogui.locateOnScreen('./image/accept.png', grayscale = True, confidence = 0.8)
        if keyboard.is_pressed('esc'):
            cancel()
    pyautogui.moveTo(a)
    pyautogui.doubleClick()
    os.system('cls')
    exit()
    
def cancel():
    c = pyautogui.locateOnScreen('./image/cancel.png', confidence = 0.9)
    pyautogui.moveTo(c)
    pyautogui.click()
    print('Queue Has Been Canceled')
    os.system('cls')
    wait()

def wait():
    print('Press Space To Queue')
    print()
    print('Press ESC To Close Program')
    wait = 0
    while(wait == 0):
        if keyboard.is_pressed('space'):
            os.system('cls')
            find()
        if keyboard.is_pressed('esc'):
            os.system('cls')
            exit()

find()
accept()