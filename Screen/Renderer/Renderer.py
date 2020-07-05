import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
#import cairo # Change Location of virtual-enviroment to have cairo in atom
class Renderer(tk.Frame):
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master


    def DrawObject(self, Object):
        """ DrawObject will draw the object of which one puts as argument. This has to be the full path! """

        pass
print(os.getcwd())
