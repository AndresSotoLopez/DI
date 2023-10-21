from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import DetailWindow

class MainWindow():

    def on_button_clicked(self, cell):
        detail_window = DetailWindow(self.root, cell.title, cell.imageTk, cell.description)

    def __init__(self, root):
        
        self.root = root
        root.title("MainWindow")

        self.cells = [

            Cell("COD 4", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/cod4.png", "COD4"),
            Cell("COD MW2", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codmw2.png", "CODMW2"),
            Cell("COD MW3", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codmw3.png", "CODMW3"),
            Cell("COD BO2", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codbo2.png", "CODBO2"),
            Cell("COD BO3", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/unedited/codbo3.png", "CODBO3"),


        ]

        for i, cell in enumerate(self.cells):
          
            label = ttk.Label(root, image = cell.imageTk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = 0,column = i)
            label.bind("<Button-1>",lambda event, cell = cell: self.on_button_clicked(cell))