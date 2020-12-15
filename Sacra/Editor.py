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

events_list = []

def Render(Mesh):
    global RenderObject
    RenderObject = Renderer2(Mesh)
    RenderObject._Draw()
    print(Mesh)
    print("Done")

def _OpenFile():
    LocalDirectory = os.path.join(os.getcwd(), "Saves")
    filepath = filedialog.askopenfilename(initialdir = LocalDirectory,
    title = 'Select a file, Has to be .json format!')
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



def handle_keypress(event):
    print(event.char)

def handle_click(event):
    print("The button was clicked!")



Window = tk.Tk()
Window.title("Sacra Game Engine")
Window.geometry("1000x600")




menubar = tk.Menu(Window)

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

Window.config(menu=menubar)



Window.bind("<x>", handle_keypress)
#Open_Button = tk.Button(Window, text = "Open a file", command = _OpenFile).pack()
Window.mainloop()
