from tkinter import ttk
import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk

from cell import Cell
from detail_window import DetailWindow
    
    
#Funcion que devuelve la imagen de cada item del json    
def load_image_from_url(self, url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    return img


class MainWindow():

    def on_button_clicked(self, cell):
        detail_window = DetailWindow(self.root, cell.title, cell.imageTk, cell.description)

    def __init__(self, root, json_data):
        
        #Variables
        self.root = root
        root.title("MainWindow")
        self.cells = []

        #Centrar la ventana
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        #Bucle para recorrer todos los items del JSON descargado y añadirlo a la celda
        for item in json_data:

            #Guardamos en variables cada elemento del item del JSON
            name = item["name"]
            description = item["description"]
            img_url = item["img_url"]
            image = load_image_from_url(self, img_url)

            #creamos una nueva variable celda con los datos de la variable de arriba y la añadimos al array donde estarán todas las celdas
            cell = Cell(name, description, img_url, image)
            self.cells.append(cell)

            #Creacion de etiquetas al generar las imagenes
            label = ttk.Label(root, image=cell.imagen, text=name, compound=tk.BOTTOM)
            label.grid(row=len(self.cells) - 1, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))