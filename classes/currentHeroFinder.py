import math
import win32gui # TODO: exchange win32gui for PIL -> screenshot method
import win32api
from collections import deque

from classes.jsonReader import JsonReader

class CurrentHeroFinder:

    # target_color = (221, 80, 0)
    target_color = (235, 235, 220)

    # def __init__(self, heroes):
    #     self.heroes = heroes

    #     # Get the handle to the desktop window
    #     self.hDesktop = None
    #     # Get the device context for the entire screen
    #     self.hDC = None

    #     # self.queue = deque()

    def __init__(self):
        # Get the handle to the desktop window
        # self.hDesktop = None
        self.hDesktop = win32gui.GetDesktopWindow()
        # Get the device context for the entire screen
        # self.hDC = None
        self.hDC = win32gui.GetWindowDC(self.hDesktop)

        jsonReader = JsonReader()
        self.heroes = jsonReader.returnHeroes()

    def start(self):
        # Get the handle to the desktop window
        self.hDesktop = win32gui.GetDesktopWindow()

        # Get the device context for the entire screen
        self.hDC = win32gui.GetWindowDC(self.hDesktop)

    def getPixelColor(self, x, y):
        pixel = win32gui.GetPixel(self.hDC, x, y)
        red = pixel & 0xff
        green = (pixel >> 8) & 0xff
        blue = (pixel >> 16) & 0xff
        return [red, green, blue]
    
    def color_distance(self, color1, color2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))
    
    def are_colors_similar(self, color1, color2, threshold=10):
        distance = self.color_distance(color1, color2)
        return distance < threshold

    def findCurrentHero(self):
        for hero, properties in self.heroes.items():
            # Get the pixel value at the specified location
            pixel = win32gui.GetPixel(self.hDC, properties['positionX'], properties['positionY'])
            red = pixel & 0xff
            green = (pixel >> 8) & 0xff
            blue = (pixel >> 16) & 0xff
            print(red, green, blue)
            if self.are_colors_similar((red, green, blue), self.target_color): # if red > 230 and green > 230 and blue > 200:
                return [properties['x-index'], properties['y-index']]
                

    def terminate(self):
        # Release the device context
        win32gui.ReleaseDC(self.hDesktop, self.hDC)