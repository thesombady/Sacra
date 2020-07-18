import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
#Import Materials #Don't work when importing renderer!
from SacraMathEngine import MeshObject
from PIL import Image


class Renderer(tk.Canvas):
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master
        self.master.geometry(f'400x600')
        self.Masterpath = os.path.join(os.getcwd(), '/Saves')


    def DrawMesh(self, Mesh):
        """Draw the given mesh, also projecting it on a 2d plane."""
        if isinstance(Mesh, MeshObject):
            pass #Decide whether to make a picture and rendering that picture or draw on canvas.








Cube = """{
    "Cube" : [{
    "1" : "Triangle(vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0))"},
    {
    "2": "Triangle(vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0))"},
    {
    "3": "Triangle(vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1))"},
    {
    "4": "Triangle(vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1))"},
    {
    "5": "Triangle(vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1))"},
    {
    "6": "Triangle(vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1))"},
    {
    "7": "Triangle(vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0))"},
    {
    "8": "Triangle(vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0))"},
    {
    "9": "Triangle(vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1))"},
    {
    "10": "Triangle(vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0))"},
    {
    "11": "Triangle(vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0))"},
    {
    "12": "Triangle(vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0))"}]
}
"""


test = json.loads(Cube)



root = tk.Tk()
app = Renderer(root)
app.mainloop()
