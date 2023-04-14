import pyautogui

class InputBot:

    def __init__(self, current, target):
        # self.heroes = heroes
        self.current = current
        self.target = target

    def moveToTarget(self):
        self.moveY()
        self.moveX()
        self.dispatchInput(1, 'space')

    def moveX(self):
        currentX = self.current[0]
        targetX = self.target[0]
        # print(currentX, targetX)
        delta = targetX - currentX
        # print(delta)
        if delta < 0:
            self.dispatchInput(abs(delta), 'left')
            print(abs(delta), 'left')
        else:
            self.dispatchInput(delta, 'right')
            print(delta, 'right')

    def moveY(self):
        currentY = self.current[1]
        targetY = self.target[1]
        if currentY == 0 and targetY == 1:
            self.dispatchInput(1, 'down')
        elif currentY == 1 and targetY == 0:
            self.dispatchInput(1, 'up')

    def dispatchInput(self, times, key):
        for i in range(times):
            pyautogui.press(key)