import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
#Import Materials #Don't work when importing renderer!
import SacraMathEngine as me
from PIL import Image


class Renderer(tk.Canvas):
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master
        self.master.geometry(f'400x600')
        self.Masterpath = os.path.join(os.getcwd(), '/Saves')


    def DrawObject(self, Object, Name):
        """ DrawObject will draw the object of which one puts as argument. This requires the name of of file, not the file-extension itself. """
        #ObjectToDraw = os.path.join(self.Masterpath, Object + '.json')
        if not isinstance(Object, me.MeshObject):
            raise KeyError("Not correct format")
        RealObject = Object








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
#test = json.dumps(test, indent = 4)
print(type(test))
mesh = me.MeshObject(test, 'Cube')
print(type(mesh))


root = tk.Tk()
app = Renderer(root)
app.DrawObject(mesh, 'Cubes')
app.mainloop()
