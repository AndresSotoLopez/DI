import tkinter as tk
from PIL import Image, ImageTk

class Cell:

    def __init__(self, title, path, description):

        self.title = title
        self.path = path
        self.description = description
        img = (Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS)
        self.imageTk = ImageTk.PhotoImage(img)