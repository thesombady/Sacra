import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
#import Materials
import SacraMathEngine as me


class Renderer(tk.Frame):
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master
        self.master.geometry(f'400x600')


    def DrawObject(self, Object):
        """ DrawObject will draw the object of which one puts as argument. This has to be the full path! """
        pass


#print(me.vec3d(1,1,1))
root = tk.Tk()
app = Renderer(root)
app.mainloop()
