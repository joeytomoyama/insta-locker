import time
import pyautogui
import win32gui
import win32api
import keyboard

print('start')

active = False

# Get the handle to the desktop window
hDesktop = win32gui.GetDesktopWindow()

def listenForKey(key):
    # global active
    if key.name == 'a':
        # active = not active
        mouseLocation = pyautogui.position()

        # Get the device context for the entire screen
        hDC = win32gui.GetWindowDC(hDesktop)

        # Get the pixel value at the specified location
        # pixel = win32gui.GetPixel(hDC, x, y)
        pixel = win32gui.GetPixel(hDC, mouseLocation.x, mouseLocation.y)

        # Release the device context
        win32gui.ReleaseDC(hDesktop, hDC)

        # Print the pixel value as RGB tuple
        print("Pixel value:", (pixel & 0xff), ((pixel >> 8) & 0xff), ((pixel >> 16) & 0xff), end='; ') # 235, 100, 25
        print("Pixel position:", pyautogui.position().x, pyautogui.position().y)

keyboard.on_press(listenForKey)


while True:
    # if active == False:
    #     print('nothing happening')
    #     time.sleep(0.5)
    #     continue

    # mouseLocation = pyautogui.position()

    # # Get the device context for the entire screen
    # hDC = win32gui.GetWindowDC(hDesktop)

    # # Get the pixel value at the specified location
    # # pixel = win32gui.GetPixel(hDC, x, y)
    # pixel = win32gui.GetPixel(hDC, mouseLocation.x, mouseLocation.y)

    # # Release the device context
    # win32gui.ReleaseDC(hDesktop, hDC)

    # # Print the pixel value as RGB tuple
    # print("Pixel value:", (pixel & 0xff), ((pixel >> 8) & 0xff), ((pixel >> 16) & 0xff))
    # print("Pixel position:", pyautogui.position().x, pyautogui.position().y)

    # Wait for a short time before checking again
    time.sleep(0.5)