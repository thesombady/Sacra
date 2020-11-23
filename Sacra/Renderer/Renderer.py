import sys
import os
import json
#Import Materials #Don't work when importing renderer!
from SacraMathEngine import *
from PIL import Image, ImageDraw
import time
from concurrent.futures import ProcessPoolExecutor
from math import cos, sin
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
    def __init__(self, Object, Background = None, size = (1000, 1000), Viewer = None):
        if not isinstance(Object, MeshObject3d):
            raise TypeError('[System]: Mesh object is of wrong format')
        else:
            self.Mesh = Object
            self.size = size
            self.Background = Background
            if Viewer == None:
                self.Viewer = vec3d(-10,-10,-10)
            else:
                if isinstance(Viewer, vec3d):
                    self.Viwer = Viewer
                else:
                    print(RenderError('[System]: Cant compute Viwers position, setting it to <(-10, -10, -10)>'))
                    self.Viewer = vec3d(-10,-10,-10)

    def _Draw(self, EVector = None, Orientation = None, Frame = None):
        if Frame == None:
            Name = 'Frame2'
        else:
            Name = Frame
        Detail = 100
        try:
            path = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Sacra/Renderer/CurrentFrame', Name + '.png')
        except Exception as E:
            raise E
        Mesh = self.Mesh.Mesh
        def Projection(Vector, Orientation = vec3d(0,0,0), EVector = vec3d(100,100,100)):
            """Perspective projection formula for each point."""
            vec1 = Vector
            vec2 = self.Viewer
            if not isinstance(Orientation, (list, tuple, vec3d)):
                raise TypeError('[Orientation is of wrong type]')
            matrix1 = matrix3d(vec3d(1,0,0), vec3d(0, cos(Orientation[0]), sin(Orientation[0])), vec3d(0,-sin(Orientation[0]), cos(Orientation[1])))
            matrix2 = matrix3d(vec3d(cos(Orientation[1]), 0 , -sin(Orientation[1])), vec3d(0,1,0), vec3d(sin(Orientation[1]), 0, cos(Orientation[1])))
            matrix3 = matrix3d(vec3d(cos(Orientation[2]), sin(Orientation[2]), 0), vec3d(-sin(Orientation[2]), cos(Orientation[2]), 0), vec3d(0,0,1))
            positionvector = vec1 - vec2
            ProjectionMatrix = ((matrix1 * matrix2) * matrix3) * positionvector
            ProjectionVector = vec3d(EVector[2]/ProjectionMatrix[2] * ProjectionMatrix[0] + EVector[0], EVector[2]/ProjectionMatrix[2] * ProjectionMatrix[1] + EVector[1], 0)
            return ProjectionVector

        def NormCalculator(tri):
            if not isinstance(tri, Triangle):
                raise TypeError('[System]: Filler cant execute due to not having input as Triangle-object')
            else:
                Viewpoint = self.Viewer.normalize()
                norm = tri.normvector().normalize()
                normscalar = abs(norm.dot(Viewpoint))
                return normscalar

        def Helper(tri, image, Colour = None):
            """Draws each rectangle for the _Draw function"""
            if EVector == None or Orientation == None:
                vec1 = Projection(tri[0])._int()
                vec2 = Projection(tri[1])._int()
                vec3 = Projection(tri[2])._int()
            else:
                if isinstance(EVector, vec3d) and Orientation == None:
                    vec1 = Projection(tri[0], EVector = EVector)._int()
                    vec2 = Projection(tri[1], EVector = EVector)._int()
                    vec3 = Projection(tri[2], EVector = EVector)._int()
                elif isinstance(EVector, vec3d) and isinstance(Orientation, vec3d):
                    vec1 = Projection(tri[0], EVector = EVector, Orientation = Orientation)._int()
                    vec2 = Projection(tri[1], EVector = EVector, Orientation = Orientation)._int()
                    vec3 = Projection(tri[2], EVector = EVector, Orientation = Orientation)._int()
            NormValue = NormCalculator(tri)
            if Colour == None:
                Filler = (int(255 * NormValue), int(255 * NormValue), int(255 * NormValue))
            else:
                pass
            image.polygon(((vec1[0], vec1[1]), (vec2[0], vec2[1]), (vec3[0], vec3[1])), fill = Filler, outline = 1)
            image.line(((vec1[0], vec1[1]), (vec2[0], vec2[1])), width = 1, fill = (0,0,0))
            #image.line((vec1[0], vec1[1], vec2[0], vec2[1]), width = 1, fill = (255,0,0))
            #image.line((vec2[0], vec2[1], vec3[0], vec3[1]), width = 1, fill = (255,0,0))
            #image.line((vec3[0], vec3[1], vec1[0], vec1[1]), width = 1, fill = (255,0,0))
            image.line(((vec2[0], vec2[1]), (vec3[0], vec3[1])), width = 1, fill = (0,0,0))
            image.line(((vec1[0], vec1[1]), (vec3[0], vec3[1])), width = 1, fill = (0,0,0))
        with Image.new("RGBA", self.size) as file:
            image = ImageDraw.Draw(file)
            for i in range(len(Mesh)):
                Helper(Mesh[i], image)
            try:
                file.save(path)
            except Exception as E:
                raise E

    def _Shader(self):
        pass


if __name__ == '__main__' :
    #Tetra = MeshObject3d()._setter('tetrahydron')
    #Tetra = Tetra * 10
    #TetraRender = Renderer2(Tetra)._Draw(EVector = vec3d(100,100,100), Orientation=vec3d(0,0,0.5))
    #Cube = MeshObject3d()._setter('Cube') * 10
    #CubeRenderer = Renderer2(Cube)._Draw(EVector = vec3d(10,10,10), Orientation = vec3d(25,50,0))
    Cube1 = MeshObject3d()
    triangle1 = Triangle(vec3d(0,0,0), vec3d(0,1,0), vec3d(1,0,0))#Front
    triangle2 = Triangle(vec3d(1,0,0), vec3d(1,1,0), vec3d(0,1,0))
    triangle3 = Triangle(vec3d(0,0,0), vec3d(1,0,0), vec3d(1,0,1))#Bottom
    triangle4 = Triangle(vec3d(1,0,1), vec3d(0,0,1), vec3d(0,0,0))

    #triangle3 = Triangle(vec3d(0,1,0), vec3d(0,1,1), vec3d(0,0,1))#East
    #triangle4 = Triangle(vec3d(0,0,1), vec3d(0,0,0), vec3d(0,1,0))
    #triangle5 = Triangle(vec3d(0,1,0), vec3d(1,1,0), vec3d(1,1,1))#Top
    #triangle6 = Triangle(vec3d(1,1,1), vec3d(0,1,0), vec3d(1,1,0))
    #triangle7 = Triangle(vec3d(1,1,0), vec3d(1,0,1), vec3d())#West
