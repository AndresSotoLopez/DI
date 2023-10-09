from tkinter import Tk, ttk

def __yes_window__():

    root = Tk()

    root.title("yes_window")
    label = ttk.Label(root, text = "Opcion -> si")
    label.pack()

    root.mainloop()