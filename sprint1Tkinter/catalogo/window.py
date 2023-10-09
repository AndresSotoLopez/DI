from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell

class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda " + cell.title
        messagebox.showinfo("Información: ", message)

    def __init__(self, root):
        
        root.title("MainWindow")

        self.cells = [

            Cell("COD 4", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/edited/cod4.png"),
            Cell("COD MW2", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/edited/codmw2.png"),
            Cell("COD MW3", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/edited/codmw3.png"),
            Cell("COD BO2", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/edited/codbo2.png"),
            Cell("COD BO3", "/home/drew/DAM/Desarrollo de interfaces/DI/sprint1Tkinter/catalogo/data/edited/codbo3.png"),


        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.imageTk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=1+i)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))