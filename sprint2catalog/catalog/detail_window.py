import tkinter as tk
from tkinter import ttk

class DetailWindow:
    def __init__(self, root, title, image, description):
        
        #Variables del constructor
        self.root = root
        self.title = title
        self.image = image
        self.description = description

        #Centrar la ventana
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")


        self.window = tk.Toplevel(root)
        self.window.title(self.title)

        image_label = ttk.Label(self.window, image=self.image)
        image_label.pack()

        title_label = ttk.Label(self.window, text=self.title, font=("Roboto", 16))
        title_label.pack()
        
        description_label = ttk.Label(self.window, text=self.description, wraplength=300)
        description_label.pack()