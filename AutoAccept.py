import pyautogui
import keyboard
import os, ctypes
import time

try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if(is_admin == False):
    print('Please Run Script as Administrator')
    exit()

def find():
    os.system('cls')
    checker()
    iq = pyautogui.locateOnScreen('./image/inq.png', confidence = 0.8)
    if iq != None:
        accept()
    f = pyautogui.locateOnScreen('./image/find.png', confidence = 0.8)
    pyautogui.doubleClick(f)
    accept()

def accept():
    a = None
    print ('Waiting For Queue')
    print ()
    print ('Press Escape To Cancel Queue')
    while(a == None):
        a = pyautogui.locateOnScreen('./image/accept.png', grayscale = True, confidence = 0.8)
        if (a != None): 
            pyautogui.doubleClick(a)
        if keyboard.is_pressed('esc'):
            cancel()
        b = pyautogui.locateOnScreen('./image/emote.png', confidence = 0.9)
        if (b != None):
            exit()
    
def cancel():
    c = pyautogui.locateOnScreen('./image/cancel.png', confidence = 0.9)
    pyautogui.doubleClick(c)
    os.system('cls')
    wait()

def wait():
    logo()
    print('- Press Enter To Start Queue')
    print('- Press ESC To Close Program')
    wait = 0
    while(wait == 0):
        if keyboard.is_pressed('enter'):
            os.system('cls')
            find()
        if keyboard.is_pressed('esc'):
            os.system('cls')
            exit()

def logo():
    os.system('cls')
    print("""                _       __  __                             
     /\        | |     |  \/  |                            
    /  \  _   _| | __ _| \  / | __ _ _ __ ___   ___  _ __  
   / /\ \| | | | |/ _` | |\/| |/ _` | '__/ _ \ / _ \| '_ \ 
  / ____ \ |_| | | (_| | |  | | (_| | | | (_) | (_) | | | |
 /_/    \_\__,_|_|\__,_|_|  |_|\__,_|_|  \___/ \___/|_| |_|
                                                           
                                                           """ )
    #print("-----------------------------------------------------------")
    return()


def checker():
    cm = pyautogui.locateOnScreen('./image/cmi.png', confidence=0.8)
    pt = pyautogui.locateOnScreen('./image/party.png', confidence=0.8)
    if (pt != None):
        if (cm == None):
            pyautogui.doubleClick(pt)
            time.sleep(1.5) 
    return()

wait()