from tkinter import ttk

class main_window:

    def on_button_clicked(self):
        pass

    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Este mensaje es poco importante")
        self.label.pack()

        self.button=ttk.Button(self.root, text="Acción", command=self.on_button_clicked)
        self.button.pack()
