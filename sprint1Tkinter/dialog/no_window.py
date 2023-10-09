from tkinter import Tk, ttk

def __no_window__():

    root = Tk()
    root.title("no_window")
    label = ttk.Label(root, text = "Opcion -> no")
    label.pack()
    root.mainloop()