import pygetwindow
import pyautogui
import keyboard
import os,ctypes
import numpy as np
import time


l, t, w, h = (0,0,0,0)

def game_window_loc():
    global l, t, w, h 
    Game_Window = pygetwindow.getWindowsWithTitle('League of Legends')[0]
    l, t, w, h = Game_Window.left, Game_Window.top, Game_Window.width, Game_Window.height
    return

def wait():
    logo()
    print('- Press Enter To Start Queue')
    print('- Press ESC To Close Program')
    while True:
        if keyboard.is_pressed('enter'):
            os.system('cls')
            find()
        if keyboard.is_pressed('esc'):
            os.system('cls')
            exit()

def find():
    os.system('cls')
    checker()
    game_window_loc()
    in_queue = pyautogui.locateOnScreen('./image/inq.png', confidence = 0.8, region = (l, t, w, h))
    if in_queue != None:
        accept()
    find_button = pyautogui.locateOnScreen('./image/fbutton.png', confidence = 0.8, region = (l, t, w, h))
    if find_button != None:
        pyautogui.click(find_button)
        accept()
    else:
        accept()

def cancel():
    game_window_loc()
    cancel_queue = pyautogui.locateOnScreen('./image/cancel.png', confidence = 0.8, region = (l, t, w, h))
    pyautogui.click(cancel_queue)
    os.system('cls')
    wait()

def accept():
    print('Waiting For Queue')
    print()
    print('Press Escape To Cancel Queue')
    while True:
        game_window_loc()
        accept_queue = pyautogui.locateOnScreen('./image/accept.png', confidence = 0.8, region = (l, t, w, h))
        if (accept_queue != None):
            pyautogui.click(accept_queue)
        if keyboard.is_pressed('esc'):
            cancel()
        close_auto_accept = pyautogui.locateOnScreen('./image/emote.png', confidence = 0.8, region = (l, t, w, h))
        if (close_auto_accept != None):
            exit()

def checker():
    game_window_loc()
    change_mode = pyautogui.locateOnScreen('./image/cmi.png', confidence = 0.8, region = (l, t, w, h))
    party_image = pyautogui.locateOnScreen('./image/party.png', confidence = 0.8, region = (l, t, w, h))
    if (party_image !=None):
        if (change_mode == None):
            pyautogui.click(party_image)
            time.sleep(1.5)
    return

def logo():
    os.system('cls')
    print("""                _       __  __                             
     /\        | |     |  \/  |                            
    /  \  _   _| | __ _| \  / | __ _ _ __ ___   ___  _ __  
   / /\ \| | | | |/ _` | |\/| |/ _` | '__/ _ \ / _ \| '_ \ 
  / ____ \ |_| | | (_| | |  | | (_| | | | (_) | (_) | | | |
 /_/    \_\__,_|_|\__,_|_|  |_|\__,_|_|  \___/ \___/|_| |_|
                                                           
                                                           """ )
    return

wait()