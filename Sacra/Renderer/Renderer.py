import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
#Import Materials #Don't work when importing renderer!
from SacraMathEngine import *
from PIL import Image


class RenderError(Exception):
    pass

class Renderer:
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """
    def __init__(self, Object):
        if not isinstance(Object, MeshObject):
            raise RenderError("Cannot load MeshObject")
        else:
            self.Object = Object

    def DrawObject(self):
        pass
