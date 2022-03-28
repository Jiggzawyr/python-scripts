from PIL import Image, ImageGrab 
import os
import time
import win32api, win32con, win32gui

# Globals
# ------------------
 
x_pad = 390
y_pad = 490

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('Click.')          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def startGame():
    #location of first menu
    mousePos((300, 200))
    leftClick()
    time.sleep(.4)
     
    #location of second menu
    mousePos((300, 390))
    leftClick()
    time.sleep(.4)
     
    #location of third menu
    mousePos((570, 450))
    leftClick()
    time.sleep(.4)
     
    #location of fourth menu
    mousePos((320, 380))
    leftClick()
    time.sleep(.4)
 
def focusGame():

    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    samsungGameWindow = [(hwnd, title) for hwnd, title in winlist if 'edge' in title.lower()]

    print('samsungGameWindow:')
    print(samsungGameWindow)

    # just grab the hwnd for first window matching samsungGameWindow
    samsungGameWindow = samsungGameWindow[0]
    hwnd = samsungGameWindow[0]

    win32gui.SetForegroundWindow(hwnd)

def main():

    focusGame()
    startGame()

    
 
if __name__ == '__main__':
    main()