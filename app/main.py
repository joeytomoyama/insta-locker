import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic UI with Buttons")
        self.root.geometry("500x400")  # Set the default window size

        # Create a container frame for the buttons and center it
        self.container_frame = tk.Frame(root)
        self.container_frame.pack(side=tk.TOP, pady=10)

        # Create the buttons inside the container frame
        self.button1 = tk.Button(self.container_frame, text="Page 1", command=self.show_page1)
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2 = tk.Button(self.container_frame, text="Page 2", command=self.show_page2)
        self.button2.pack(side=tk.LEFT, padx=10)

        self.button3 = tk.Button(self.container_frame, text="Page 3", command=self.show_page3)
        self.button3.pack(side=tk.LEFT, padx=10)

        # Frame for displaying different pages
        self.page_frame = tk.Frame(root)
        self.page_frame.pack(fill=tk.BOTH, expand=True)

        self.show_page1()  # Show the first page by default

    def clear_page(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()

    def show_page1(self):
        self.clear_page()
        tk.Label(self.page_frame, text="Choose your hero", font=("Helvetica", 24)).pack(pady=20)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)
        tk.Button(self.page_frame, text="Button A1").pack(pady=10)
        tk.Button(self.page_frame, text="Button A2").pack(pady=10)

    def show_page2(self):
        self.clear_page()
        tk.Label(self.page_frame, text="Calibrate", font=("Helvetica", 24)).pack(pady=20)
        tk.Entry(self.page_frame).pack(pady=10)
        tk.Button(self.page_frame, text="Submit").pack(pady=10)

    def show_page3(self):
        self.clear_page()
        tk.Label(self.page_frame, text="Settings", font=("Helvetica", 24)).pack(pady=20)
        tk.Checkbutton(self.page_frame, text="Option 1").pack(pady=5)
        tk.Checkbutton(self.page_frame, text="Option 2").pack(pady=5)
        tk.Checkbutton(self.page_frame, text="Option 3").pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()