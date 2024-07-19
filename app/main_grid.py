import tkinter as tk
import threading
import keyboard

from classes.jsonReader import JsonReader
from classes.currentHeroFinder import CurrentHeroFinder

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic UI with Buttons")
        self.root.geometry("1400x400")  # Set the default window size

        self.selected_hero = None

        # Create a container frame for the buttons and center it
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.TOP, pady=10)

        self.button1 = tk.Button(self.button_frame, text="Heroes", command=self.show_page1)
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2 = tk.Button(self.button_frame, text="Calibrate", command=self.show_page2)
        self.button2.pack(side=tk.LEFT, padx=10)

        self.button3 = tk.Button(self.button_frame, text="Settings", command=self.show_page3)
        self.button3.pack(side=tk.LEFT, padx=10)
        
        self.hero_label = tk.Label(root, text="No hero selected", font=("Helvetica", 12))
        self.hero_label.pack(side=tk.BOTTOM, pady=10)

        jsonReader = JsonReader()
        self.heroes = jsonReader.returnHeroes()

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
        keyboard.on_press(self.keypress_handler)
        keyboard.wait()  # This will keep the thread alive to listen for keypresses

    def keypress_handler(self, e):
        if e.name != 'f1':
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
            # ip = InputBot(currentHero, targetHero)
            # ip.moveToTarget()
            return

        # Schedule the next call in n milliseconds
        self.repeated_call = self.root.after(10, self.run_main_function)

    def stop_main_function(self):
        # Stop the repeated calls
        if self.repeated_call:
            print('canceling')
            self.root.after_cancel(self.repeated_call)

    # UI stuff
    def create_page1(self):
        page1 = tk.Frame(self.root)
        # page1.grid(row=0, column=0, columnspan=2, pady=10)
        page1.columnconfigure(0, weight=1)
        page1.columnconfigure(1, weight=1)
        # tk.Label(page1, text="This is Page 1", font=("Helvetica", 24)).grid(row=0)
        
        # create all the hero buttons
        for key, value in self.heroes.items():
            sticky = 'e'
            if value['x-index'] == 0:
                sticky = 'ew'

            index = 0
            tk.Button(page1, text=key, command=lambda k=key: self.hero_label.config(text=k)).grid(row=value['y-index'], column=value['x-index'], padx=5, pady=10, sticky=sticky)

            index = index + 1   # increment index

        return page1

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
