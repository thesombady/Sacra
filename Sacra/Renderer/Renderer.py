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

    def __init__(self, Object, Background = None, size = (100, 100)):
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
                    #vec1 = self.ProjectionMatrix.Multiplcation(triangle[0])
                    #vec2 = self.ProjectionMatrix.Multiplcation(triangle[1])
                    #vec3 = self.ProjectionMatrix.Multiplcation(triangle[2])
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
                    """
                    vec1 = mesh[i][0]
                    vec2 = mesh[i][1]
                    vec3 = mesh[i][2]
                    projvec1 = self.ProjectionMatrix.Multiplcation(vec1)
                    projvec2 = self.ProjectionMatrix.Multiplcation(vec2)
                    projvec3 = self.ProjectionMatrix.Multiplcation(vec3)
                    """
                    #This solutions does not work as of yet
                    """
                    ProjectedTriangle = []
                    for j in range(0,len(mesh[i]) - 1):
                        vec = self.ProjectionMatrix.Multiplcation(mesh[i][j])
                        vec = (vec4d(0,0,0,0) - vec) * 10
                        file.putpixel((int(vec[0]), int(vec[1])), (255,255,255))
                        #print(projvec * 10)
                    """
                    """"
                    TransformedVectors = []
                    for vec in mesh[i]:
                        TransformedVectors.append(self.ProjectionMatrix.Multiplcation(vec))
                    DrawTriangle(TransformedVectors, image = image)
                    """
                    HelperDraw(mesh[i], image)


                file.save(FilePath)
                pass #Sucessfully saved an image!
        except:
            raise RenderError('[System]: Can not create frame.')

        return type(Name)


Cube = MeshObject()
Cube.setter('test')
Cube = Cube + vec3d(1,1,1)

Renderer(Cube).DrawObject(Detail = 1000)
