import tkinter as tk
from PIL import Image, ImageTk
import os

class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.width = 800
        self.height = 500
        self.title = 'Exodus Game Engine'
        self.initalize()


    def initalize(self):
        self.master.geometry(f'{self.width}x{self.height}')
        self.master.title(self.title)
        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar)
        filemenu.add_command(label = "Open", command = self.openfile)
        filemenu.add_command(label = "Save")
        filemenu.add_command(label = "Exit")
        filemenu.add_command(label = "New", command = self.newfile)

        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)

    def newfile(self):
        CreateNewFile()


    def openfile(self):
        Openfiles = OpenAFile()

class OpenAFile(tk.Toplevel):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.initalize()

    def initalize(self):
        path = '/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves'
        os.chdir(path)
        print(os.getcwd())
        for file in os.listdir():
            label = tk.Label(self.master, text = file)
            label.pack()

class CreateNewFile(tk.Toplevel):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.path = '/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves'
        self.initialize()

    def initialize(self):
        label = tk.Label(text = "Name Mesh")
        label.pack()
        self.name = tk.Entry()
        name.pack()
        button = tk.Button(text = "Create", command = self.getname)
        button.pack()

    def getname(self):
        name = self.name.get()
        print(name)
        """
        if name is in os.listdir(self.path):
            label = tk.Label(text = "Name is occupied")
        else:
            os.path.join(self.path, paths)
        """


root = tk.Tk()
app = Application(root)
app.mainloop()
