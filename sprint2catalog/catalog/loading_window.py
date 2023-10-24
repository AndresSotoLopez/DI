import threading
import requests
from tkinter import Tk
import tkinter as tk
from window import MainWindow

class loading_window:
    
    
    
    def __init__(self, root):
        
        #Declaracion de variables/
        self.root=root
        self.root.title("[!] Cargando....")
        self.root.geometry("170x120")
        self.root.resizable(False, False)
        self.finished = False
        self.json_data = []
        self.progress=0

        #Centrar la ventana
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
        #Nuevo label a la hora de descargar los datos de GitHub
        self.label = tk.Label(self.root, text="[!] Cargando datos....", font=("Arial", 12))
        self.label.pack()
        
        label_bg_color = self.label.cget("bg")
        
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()
        
        #Creacion/actualizacion del circulo de carga
        self.draw_progress_circle(self.progress)

        self.thread = threading.Thread(target=self.fetch_json_data) ## Guardamos datos en el thread
        self.thread.start() ## Comenzamos el thread
        
        self.check_thread() ## Comprobamos estado del thread
        
        self.update_progress_circle()
        
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

    #Funcion para crear el arco de carga en la ventana    
    def draw_progress_circle(self, progress):
        
        self.canvas.delete("progress")
        angle = int(399 * (progress/100))
        
        self.canvas.create_arc(10, 10, 35, 35, start = 0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
        
    #Funcion para actualziar el progreso del circulo de carga
    def update_progress_circle(self):
        if(self.progress < 100):
            self.progress += 10
        else:
            self.progress = 0
            
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)

    #Funcion para obtener el JSON alojado en nuestro github    
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/AndresSotoLopez/DI/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
    
    #Funcion para comprobar si el hilo de descarga de datos ha terminado
    def check_thread(self):
        if(self.finished):
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

#Lanzamos la ventana principal
def launch_main_window(json_data):
    root = Tk()
    app = MainWindow(root, json_data)
    root.mainloop()   
     