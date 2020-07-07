import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
#import MathEngine as me #Might change this
#import cairo # Change Location of virtual-enviroment to have cairo in atom
#import MathEngine as me # needs this package to get the convertion and suchs
"""
from .MathEngine.Vector import vec3d
from .MathEngine.Matrix import matrix3d
from .MathEngine.Triangle import triangle, MeshObject
#The above three imports are to make the program.py to work, below will be imports to test this program.
"""
import MathEngine as me

class Renderer(tk.Frame):
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master


    def DrawObject(self, Object):
        """ DrawObject will draw the object of which one puts as argument. This has to be the full path! """

        pass

print(me.vec3d(1,1,1))