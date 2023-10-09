from tkinter import Tk, ttk
from no_window import __no_window__
from yes_window import __yes_window__

class main_window():

    def onButtonClicked(self):

        pass

    def __init__(self, root):
        
        self.root = root
        root.title("main_window")

        #Frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        #Label
        self.label = ttk.Label(self.frame, text = "Un texto cualquiera")
        self.label.pack()

        #Boton
        self.button1 = ttk.Button(self.frame, text = "Yes", command = __yes_window__)
        self.button1.pack(side = "left")

        self.button2 = ttk.Button(self.frame, text = "No", command = __no_window__)
        self.button2.pack(side = "right", padx = 5)