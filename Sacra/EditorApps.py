import tkinter as tk
from tkinter import ttk

def Construct(App):
    try:
        Rotate = ttk.Button(master = App, text = "Rotate")
        Rotate.place(x = 10, y = 0)
    except Exception as E:
        raise E
