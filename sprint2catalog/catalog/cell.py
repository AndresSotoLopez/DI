import tkinter as tk
from PIL import Image, ImageTk

class Cell:

    def __init__(self, name, descripcion, image_url, imagen):
        
        self.name = name
        self.descripcion = descripcion
        self.image_url = image_url
        self.imagen = imagen      