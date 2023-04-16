import pyautogui

class InputBot:

    def __init__(self, current, target):
        self.current = current
        self.target = target

    def moveToTarget(self):
        self.moveX()
        self.moveY()
        self.dispatchInput(1, 'space')

    def moveX(self):
        currentX = self.current[0]
        targetX = self.target[0]
        delta = targetX - currentX
        if delta < 0:
            self.dispatchInput(abs(delta), 'left')
        else:
            self.dispatchInput(delta, 'right')

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