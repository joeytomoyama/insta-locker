import threading
import time
import pyautogui
import win32gui
import win32api
import keyboard
import json
from currentHeroFinder import CurrentHeroFinder
from inputBot import InputBot

print('start')

# Define the coordinates of the bottom left pixel
x = 0
y = 0

active = False

# Define the color of the pixel to trigger the key press
white = (255, 255, 255)


# # Get the handle to the desktop window
# hDesktop = win32gui.GetDesktopWindow()

# Get heroes data from json
with open('supports.json', 'r') as file:
    heroes = json.load(file)

chf = CurrentHeroFinder(heroes)

# Define the function to run continuously in the background
def run():
    global active
    while True:
        if active == False:
            print('nothing happening')
            time.sleep(0.5)
            continue

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

        currentHero = chf.findCurrentHero()
        print(currentHero)
        print(type(currentHero))
        if type(currentHero) == list:
            ip = InputBot(currentHero, [13, 1])
            # ip = InputBot([1, 1], [13, 1])
            ip.moveToTarget()
            active = False

        # return

        # Wait for a short time before checking again
        time.sleep(0.5)


# run()

def listenForKey(key):
    global active
    if key.name == 'a':
        active = not active

keyboard.on_press(listenForKey)

# Create a new thread and start running the function in the background
thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

# Program will continue to run in the background indefinitely
while True:
    time.sleep(0.5)