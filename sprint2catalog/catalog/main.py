from tkinter import Tk
from window import MainWindow
from loading_window import loading_window

if __name__ == "__main__":

    root = Tk()
    app = loading_window(root)
    #app = MainWindow(root)
    root.mainloop()
  