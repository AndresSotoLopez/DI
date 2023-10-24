from tkinter import ttk
import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk

from cell import Cell
from detail_window import DetailWindow
    
    
def load_image_from_url(self, url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    return img


class MainWindow():

    def on_button_clicked(self, cell):
        detail_window = DetailWindow(self.root, cell.title, cell.imageTk, cell.description)

    def __init__(self, root, json_data):
        
        self.root = root
        root.title("MainWindow")

        self.cells = []

        for item in json_data:

            name = item["name"]
            description = item["description"]
            img_url = item["img_url"]
            image = load_image_from_url(self, img_url)

            cell = Cell(name, description, img_url, image)
            self.cells.append(cell)

            label = ttk.Label(root, image=cell.imagen, text=name, compound=tk.BOTTOM)
            label.grid(row=len(self.cells) - 1, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))