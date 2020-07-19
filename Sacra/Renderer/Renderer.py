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
