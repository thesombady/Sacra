import sys
import os
import json
#Import Materials #Don't work when importing renderer!
from SacraMathEngine import *
from PIL import Image, ImageDraw
import time
from concurrent.futures import ProcessPoolExecutor
#Will use above import too speed up the rendering time
#Will use exec as input in editor

class RenderError(Exception):
    pass

class Renderer:
    """Renderer Class; Lies inside a Frame in tkinter. The renderer will draw the shapes corresponding to each mesh. """

    def __init__(self, Object, Background = None, size = (1000, 1000)):
        if not isinstance(Object, MeshObject):
            raise RenderError("Cannot load MeshObject")
        else:
            self.size = size
            self.Object = Object
            self.ProjectionMatrix = ProjectionMatrix(size = (1000,1000)) #This is given as a default setting, can add settings later
            if Background == None:
                self.Background = Background
                #Add lightsource afterwards. Also implement which material it should have. Take either the dot-product or the crossproduct
                #to determine the intensity of the object.
            else:
                try:
                    self.Background = os.path.join(os.getcwd(), 'Sacra/Renderer/CurrentFrame', Background)
                except:
                    raise RenderError('[System]: Cannot load Background argument, either path does not exist')

    def __str__(self):
        return f'[System]: Cannot print the rendered object.'

    def LoadBackground(self):
        if self.Background == None:
            pass
        else:
            try:
                pass
            except:
                raise RenderError('[System]: Cannot load Background argument, either path does not exist')

    def DrawObject(self, Name  = 'Frame', Detail = 10):
        Path = os.path.join(os.getcwd(), 'Sacra/Renderer/CurrentFrame')
        FilePath = os.path.join(Path, Name + '.png')
        if not isinstance(Detail, int):
            raise RenderError('[System]: Cannot draw Image, the detail argument has to be of int type.')
        mesh = self.Object.Mesh #Will return the mesh of which one has intalized.
        """Well performe the projection transformation and after that we'll only the x and y coordinate!!! """

        def HelperDraw(triangle, image = None):
            """Helper function that draws each triangle."""
            if image == None:
                raise RenderError("[System]: Cant find Frame.")
            elif not isinstance(image, ImageDraw.ImageDraw):
                raise RenderError("[System]: Cannot draw triangles.")
            else:
                try:
                    #vec1 = self.ProjectionMatrix.Multiplcation(triangle[0]) * 10
                    #vec2 = self.ProjectionMatrix.Multiplcation(triangle[1]) * 10
                    #vec3 = self.ProjectionMatrix.Multiplcation(triangle[2]) * 10
                    #print(type(vec1), type(vec2), type(vec3))
                    vec1 = triangle[0] * 10
                    vec2 = triangle[1] * 10
                    vec3 = triangle[2] * 10
                    image.line([(vec1[0], vec1[1]), (vec2[0], vec2[1])])
                    image.line([(vec2[0], vec2[1]), (vec3[0], vec3[1])])
                    image.line([(vec1[0], vec1[1]), (vec3[0], vec3[1])])
                except:
                    raise RenderError('[System]: Cannot draw triangles. The helper function failed')

        try:
            with Image.new("RGB", self.size) as file:
                image = ImageDraw.Draw(file)
                for i in range(len(mesh)):
                    HelperDraw(mesh[i], image)


                file.save(FilePath)
                pass #Sucessfully saved an image!
        except:
            raise RenderError('[System]: Can not create frame.')

        return type(Name)

"""
Cube = MeshObject()
Cube.setter('test')
Cube = Cube + vec3d(1,1,1)
"""
#Renderer(Cube).DrawObject(Detail = 1000)
class Renderer2():
    def __init__(self, Object, Background = None, size = (1000, 1000)):
        if not isinstance(Object, MeshObject3d):
            raise TypeError('[System]: Mesh object is of wrong format')
        else:
            self.Mesh = Object
            self.size = size
            self.Background = Background

    def _Draw(self):
        Name = 'Frame2'
        Detail = 100
        try:
            path = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Sacra/Renderer/CurrentFrame', Name + '.png')
        except Exception as E:
            raise E
        Mesh = self.Mesh.Mesh
        def Helper(tri, image):
            #vec1 = (tri[0] * 100) + vec3d(self.size[0]/500, self.size[1]/500, 0) * 10
            vec1 = (tri[0] * 100) + vec3d(self.size[0]/self.size[1], self.size[1]/self.size[0], 0) * 100
            vec2 = (tri[1] * 100) + vec3d(self.size[0]/self.size[1], self.size[1]/self.size[0], 0) * 100
            vec3 = (tri[2] * 100) + vec3d(self.size[0]/self.size[1], self.size[1]/self.size[0], 0) * 100
            image.line([(vec1[0], vec1[1]), (vec2[0], vec2[1])])
            image.line([(vec2[0], vec2[1]), (vec3[0], vec3[1])])
            image.line([(vec1[0], vec1[1]), (vec3[0], vec3[1])])
        with Image.new("RGB", self.size) as file:
            image = ImageDraw.Draw(file)
            for i in range(len(Mesh)):
                Helper(Mesh[i], image)
            try:
                file.save(path)
            except Exception as E:
                raise E




Tetra = MeshObject3d()._setter('tetrahydron')
TetraRender = Renderer2(Tetra)._Draw()
