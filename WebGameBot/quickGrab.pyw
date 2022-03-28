from PIL import Image, ImageGrab 
import os
import time
import win32gui

# Globals
# ------------------
 
x_pad = 390
y_pad = 490

def screenGrab(hwnd):

    print('hwnd:')
    print(hwnd)


    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    box = (x_pad,y_pad,x_pad+640,y_pad+478)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '\\full_snap__.png', 'PNG')
 
def main():

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

    screenGrab(hwnd)

    
 
if __name__ == '__main__':
    main()