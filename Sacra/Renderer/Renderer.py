import sys
import os
import json
#Import Materials #Don't work when importing renderer!
from SacraMathEngine import *
from PIL import Image, ImageDraw
import time
#from concurrent.futures import ProcessPoolExecutor
#Will use above import too speed up the rendering time



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
        with Image.new("RGB", self.size) as file:
            for i in range(len(mesh)):
                """
                vec1 = mesh[i][0]
                vec2 = mesh[i][1]
                vec3 = mesh[i][2]
                projvec1 = self.ProjectionMatrix.Multiplcation(vec1)
                projvec2 = self.ProjectionMatrix.Multiplcation(vec2)
                projvec3 = self.ProjectionMatrix.Multiplcation(vec3)
                """
                #This solutions does not work as of yet
                ProjectedTriangle = []
                for j in range(0,len(mesh[i]) - 1):
                    vec = self.ProjectionMatrix.Multiplcation(mesh[i][j])
                    vec2 = self.ProjectionMatrix.Multiplcation(mesh[i][j + 1])
                    vec = vec * 100
                    vec = vec.line(vec2, Detail)
                    ProjectedTriangle.append(vec)#Just scaling it so it wont matter with small digits for now
                for j in range(len(ProjectedTriangle)):
                    for k in range(len(ProjectedTriangle[j])):
                        vec = ProjectedTriangle[j][k]
                        file.putpixel((int(vec[0]), int(vec[1])), (255,255,255))
                    #print(projvec * 10)
            file.save(FilePath)
            pass #Sucessfully saved an image!

        return type(Name)


Cube = MeshObject()
Cube.setter('test')
Cube = Cube + vec3d(1,1,1)

Renderer(Cube).DrawObject(Detail = 1000)
