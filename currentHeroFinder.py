import json
import win32gui
import win32api
from collections import deque

# # Get heroes data from json
# with open('supports.json', 'r') as file:
#     heroes = json.load(file)

class CurrentHeroFinder:

    def __init__(self, heroes):
        self.heroes = heroes

        # Get the handle to the desktop window
        self.hDesktop = win32gui.GetDesktopWindow()

        # Get the device context for the entire screen
        self.hDC = win32gui.GetWindowDC(self.hDesktop)

        self.queue = deque()

    def findCurrentHero(self):
        for hero, properties in self.heroes.items():
            # Get the pixel value at the specified location
            pixel = win32gui.GetPixel(self.hDC, properties['position'][0], properties['position'][1])
            red = pixel & 0xff
            green = (pixel >> 8) & 0xff
            blue = (pixel >> 16) & 0xff
            if red > 230 and green > 230 and blue > 200:
                # return [properties['x-index'], properties['y-index']]

                self.queue.append([properties['x-index'], properties['y-index']])
                # self.queue.append(hero)
                if len(self.queue) > 3:
                    self.queue.popleft()
                
        if len(self.queue) >= 3:
            if self.queue[0] == self.queue[1] and self.queue[0] == self.queue[2]:
                print(self.queue[0])
                return self.queue[0]
                

    def terminate(self):
        # Release the device context
        win32gui.ReleaseDC(self.hDesktop, self.hDC)
        
            

d = deque()

d.append(1)
d.append(2)

print(d[1])