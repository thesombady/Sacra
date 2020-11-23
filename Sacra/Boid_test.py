from SacraMathEngine import *
from Renderer import Renderer2 as re
import os
import tkinter as tk
from PIL import ImageTk, Image
import time
from concurrent.futures import ProcessPoolExecutor


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("1000x1000")
        self.Boid = MeshObject3d()._setter("tetrahydron0")
        self.Image()

    def BoidTest(self):
        self.Boid += vec3d(1,-1,1)
        self.Boid

    def Image(self):
        Directory = os.getcwd()
        FrameFile = os.path.join(Directory, 'Sacra/Renderer/CurrentFrame/Frame2.png')
        img = ImageTk.PhotoImage(Image.open(FrameFile))
        label = tk.Label(master = self.master, image = img)
        label.image = img
        label.pack()

    def update(self):
        self.BoidTest()




root = tk.Tk()
test = App(root)
i=0
while i < 15:
    test.update()
    time.sleep(0.5)
    i += 1
