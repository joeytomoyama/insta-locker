import threading
import time
import keyboard
from classes.currentHeroFinder import CurrentHeroFinder
from classes.inputBot import InputBot
from classes.jsonReader import JsonReader

print('start')

active = False
startTime = None

jsonReader = JsonReader()
heroes = jsonReader.returnHeroes()
activationKey = jsonReader.returnActivationKey()
targetHero = jsonReader.returnTargetHero()

chf = CurrentHeroFinder(heroes)

# Define the function to run continuously in the background
def run():
    global active
    global startTime
    while True:
        if active == False:
            print('waiting for activation')
            chf.terminate()
            time.sleep(0.5)
            continue

        if startTime == None:
            startTime = time.time()

        chf.start()
        currentHero = chf.findCurrentHero()

        if type(currentHero) == list:
            print('hero found')
            ip = InputBot(currentHero, targetHero)
            ip.moveToTarget()
            active = False
            startTime = None
        else:
            print('hero not found')
            ellapsed = int(time.time()) - int(startTime)
            if ellapsed > 15: # should be a setting
                startTime = None
                active = False

        # Wait for a short time before checking again
        time.sleep(0.08)


def listenForKey(key):
    global active
    if key.name == '0':
        # active = not active
        active = True

keyboard.on_press(listenForKey)

# Create a new thread and start running the function in the background
thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

# Program will continue to run in the background indefinitely
while True:
    time.sleep(0.5)