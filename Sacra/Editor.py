import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from tkinter.filedialog import askopenfilename
import os, sys
import json, functools
from PIL import Image, ImageTk
import functools, time
from concurrent.futures import ProcessPoolExecutor
from Renderer import *  #Not done
import SacraMathEngine as me
import SacraPhysicsEngine as pe
#import Audio
import threading
global RotateMesh
#from EditorApps import Construct

events_list = []
Size = (1000, 600)
def RotateMesh():
    print("called Rotate")

def UpdateFrame(func):
    """A Decorator to update frames"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args)
            Window._PlaceFrame()
        except Exception as e:
            raise e
    return wrapper

class RenderWindow(tk.Frame):
    """A small class to have the allow for rendering."""
    def __init__(self, master, Size = (1000, 600)):
        super().__init__(master)
        self.Size = (Size[0]/2, Size[1])
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white", font = ('Helvetica', 12))
        self.master = master
        self._PlaceFrame()

    def _PlaceFrame(self, frame = "Frame2.png"):
        try:
            Path = os.path.join(os.getcwd(), f"Sacra/Renderer/CurrentFrame/{frame}")
            img = ImageTk.PhotoImage(Image.open(Path))
            label = tk.Label(master = self.master, image = img)
            label.image = img
            label.place(x = self.Size[0], y = 0)
        except Exception as e:
            raise e




def Render(Mesh):
    global RenderObject
    RenderObject = Renderer2(Mesh, size = (int(Size[0]/2), Size[1]))
    RenderObject._Draw()

def _OpenFile():
    global Mesh
    LocalDirectory = os.path.join(os.getcwd(), "Saves")
    filepath = filedialog.askopenfilename(initialdir = LocalDirectory,
    title = 'Select a file, Has to be .json format!')
    print(filepath)
    if not filepath:
        return None
    else:
        print(filepath)
        Mesh = me.MeshObject3d()
        try:
            Mesh = Mesh._setter(filepath)
        except Exception as e:
            raise e
    Render(Mesh)
    Window = RenderWindow(App)
    Window.place(x = int(Size[0]/2), y = 0)




def handle_keypress(event):
    print(event.char)

def handle_click(event):
    print("The button was clicked!")



App = tk.Tk()
App.title("Sacra Game Engine")
App.geometry(f"{Size[0]}x{Size[1]}")
#AllWidgets = Widgets(App, Size = Size)
#AllWidgets.place(x = 0, y = -10)
Construct(App)



#Rotate = ttk.Button(master = App, text = "Rotate")
#Rotate.place(x = 10, y = 0)

menubar = tk.Menu(App)

FileMenu = tk.Menu(menubar)
EditMenu = tk.Menu(menubar)
ViewMenu = tk.Menu(menubar)
BuildMenu = tk.Menu(menubar)
show_all = tk.BooleanVar()

#BuildMenu.add_checkbutton(label = "Make Client-server", onvalue = 1, offvalue = 0, variable = show_all)
#BuildMenu.add_command(label = "Build Game", command = self.BuildGame)
#menubar.add_cascade(label = "Build", menu = BuildMenu)

FileMenu.add_command(label = "Open", command = _OpenFile)
FileMenu.add_command(label = "Save")
FileMenu.add_command(label = "Exit")
FileMenu.add_command(label = "New")

menubar.add_cascade(label = "File", menu = FileMenu)
#Add space and breaker

EditMenu.add_command(label = "Add vertex")
EditMenu.add_command(label = "Edit Map")
EditMenu.add_command(label = "Move Object")

EditMenu.add_cascade(label = "Merge Objects")
menubar.add_cascade(label = 'Edit', menu = EditMenu) #Add edit commands
#Add space and breaker

ViewMenu.add_command(label = "View object")
ViewMenu.add_command(label = "Inspect object") #
menubar.add_cascade(label = "View", menu = ViewMenu)

App.config(menu=menubar)

App.bind("<x>", handle_keypress)
#Open_Button = tk.Button(Window, text = "Open a file", command = _OpenFile).pack()
App.mainloop()
