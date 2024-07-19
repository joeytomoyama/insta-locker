import tkinter as tk
import threading
import keyboard
from pynput import mouse

from classes.jsonReader import JsonReader
from classes.inputBot import InputBot
from classes.currentHeroFinder import CurrentHeroFinder

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Joey's OW2 insta locker")
        self.root.geometry("1400x400")  # Set the default window size
        self.root.resizable(False, False) # Disable window resizing

        self.jsonReader = JsonReader()
        self.inputBot = InputBot()

        # Create a container frame for the buttons and center it
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.TOP, pady=10)

        self.button1 = tk.Button(self.button_frame, text="Heroes", command=self.show_page1)
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2 = tk.Button(self.button_frame, text="Calibrate", command=self.show_page2)
        self.button2.pack(side=tk.LEFT, padx=10)

        self.button3 = tk.Button(self.button_frame, text="Settings", command=self.show_page3)
        self.button3.pack(side=tk.LEFT, padx=10)
        
        self.hero_label = tk.Label(root, text=self.jsonReader.returnTargetHero(), font=("Helvetica", 12))
        self.hero_label.pack(side=tk.BOTTOM, pady=10)

        self.heroes = self.jsonReader.returnHeroes()

        self.chf = CurrentHeroFinder()

        # Create the frames for different pages
        self.page1 = self.create_page1()
        self.page2 = self.create_page2()
        self.page3 = self.create_page3()

        self.show_page1()  # Show the first page by default

        self.startup()

    def startup(self):
        # Start a thread to listen for global key events
        listener_thread = threading.Thread(target=self.listen_for_keys, daemon=True)
        listener_thread.start()

    def listen_for_keys(self):
        keyboard.on_press(self.on_keypress)
        keyboard.wait()  # This will keep the thread alive to listen for keypresses

    def on_keypress(self, e):
        if e.name != 'f3':
            return
        
        # Start looking for pixels
        self.root.after(10, self.run_main_function)
        # Stop looking for pixels
        self.root.after(5000, self.stop_main_function)

    def run_main_function(self):
        # Function to be run repeatedly
        # self.chf.start()
        print('finding')
        currentHero = self.chf.findCurrentHero()

        if type(currentHero) == list:
            print('hero found')
            targetHero = self.jsonReader.returnTargetHeroPos()
            print(currentHero)
            print(targetHero)
            self.inputBot.moveToTarget(currentHero, targetHero)
            return

        # Schedule the next call in n milliseconds
        self.repeated_call = self.root.after(10, self.run_main_function)

    def stop_main_function(self):
        # Stop the repeated calls
        try:
            if self.repeated_call:
                print('canceling')
                self.root.after_cancel(self.repeated_call)
        except Exception:
            pass

    # UI STUFF
    def create_page1(self):
        page1 = tk.Frame(self.root)
        page1.columnconfigure(0, weight=1)
        page1.columnconfigure(1, weight=1)
        # tk.Label(page1, text="This is Page 1", font=("Helvetica", 24)).grid(row=0)
        
        # create all the hero buttons
        for key, value in self.heroes.items():
            index = 0
            tk.Button(page1, text=key, command=lambda k=key: self.page1_button_fun(k)).grid(
                row=value['y-index'], column=value['x-index'], padx=5, pady=10
            )

            index = index + 1   # increment index

        tk.Button(page1, text='Calibrate', command=self.activate_calibration_mode).grid(
            row=4, column=0, padx=5, pady=180
        )

        return page1
    
    def activate_calibration_mode(self):
        # Function to handle mouse click events
        def on_click(x, y, button, pressed):
            if pressed:
                print(f"Mouse clicked at ({x}, {y}) with {button}")

                hero = self.jsonReader.returnTargetHero()
                self.jsonReader.setHeroXY(hero, x, y)
                print("color: " + str(self.chf.getPixelColor(x, y)))

                # Stop the listener
                return False

        # Set up the mouse listener
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
    
    def page1_button_fun(self, hero):
        self.hero_label.config(text=hero)
        self.jsonReader.setTargetHero(hero)

    def create_page2(self):
        page2 = tk.Frame(self.root)
        tk.Label(page2, text="This is Page 2", font=("Helvetica", 24)).pack(pady=20)
        tk.Entry(page2).pack(pady=10)
        tk.Button(page2, text="Submit").pack(pady=10)
        return page2

    def create_page3(self):
        page3 = tk.Frame(self.root)
        tk.Label(page3, text="This is Page 3", font=("Helvetica", 24)).pack(pady=20)
        tk.Checkbutton(page3, text="Option 1").pack(pady=5)
        tk.Checkbutton(page3, text="Option 2").pack(pady=5)
        tk.Checkbutton(page3, text="Option 3").pack(pady=5)
        return page3

    def hide_all_frames(self):
        self.page1.pack_forget()
        self.page2.pack_forget()
        self.page3.pack_forget()

    def show_page1(self):
        self.hide_all_frames()
        self.page1.pack(fill=tk.BOTH, expand=True)

    def show_page2(self):
        self.hide_all_frames()
        self.page2.pack(fill=tk.BOTH, expand=True)

    def show_page3(self):
        self.hide_all_frames()
        self.page3.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
