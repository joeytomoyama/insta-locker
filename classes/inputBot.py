import pyautogui

class InputBot:

    # def __init__(self, current, target):    # change target to targetX and targetY since heroes.json change
    #     self.current = current
    #     self.target = target

    def __init__(self):
        pass

    # def moveToTarget(self):
    #     self.moveX()
    #     self.moveY()
    #     self.dispatchInput(1, 'space')

    # def moveX(self):
    #     currentX = self.current[0]
    #     targetX = self.target[0]
    #     delta = targetX - currentX
    #     if delta < 0:
    #         self.dispatchInput(abs(delta), 'left')
    #     else:
    #         self.dispatchInput(delta, 'right')

    # def moveY(self):
    #     currentY = self.current[1]
    #     targetY = self.target[1]
    #     if currentY == 0 and targetY == 1:
    #         self.dispatchInput(1, 'down')
    #     elif currentY == 1 and targetY == 0:
    #         self.dispatchInput(1, 'up')

    def moveToTarget(self, current, target):
        print('moving')
        # X
        deltaX = target[0] - current[0]
        directionX = 'right'
        if deltaX < 0:
            directionX = 'left'
        self.dispatchInput(deltaX, directionX)

        # Y
        wrongRow = target[1] != current[1]
        if wrongRow and current[1] == 0:
            self.dispatchInput(1, 'down')
        elif wrongRow and current[1] == 1:
            self.dispatchInput(1, 'up')

    def moveX(self):
        pass

    def moveY(self):
        pass

    def dispatchInput(self, times, key):
        print(f"moving {times} times to {key}")
        for i in range(abs(times)):
            pyautogui.press(key)