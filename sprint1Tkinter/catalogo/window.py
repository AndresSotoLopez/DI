from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk

class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda " + cell.title
        messagebox.showinfo("Información: ", message)

    def __init__(self, root):
        
        root.title("MainWindow")

        self.cells = [

            Cell("COD 4", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/cod4.png"),
            Cell("COD MW2", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codmw2.png"),
            Cell("COD MW3", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codmw3.png"),
            Cell("COD BO2", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codbo2.png"),
            Cell("COD BO3", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codbo3.png"),


        ]

        for i, cell in enumerate(self.cells):
           
         
            img = (Image.open(cell.path)).resize((100, 100), Image.Resampling.LANCZOS)
            cell.imagetk = ImageTk.PhotoImage(img)
            label = ttk.Label(root, image = cell.imagetk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = 0,column = i)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))