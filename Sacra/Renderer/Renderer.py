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

    def _Draw(self, EVector = vec3d(100,100,100), Orientation = vec3d(0,0,0), Frame = None):
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
        def Projection(Vector, EVector = vec3d(100,100,100), Orientation = vec3d(0,0,0)):
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
                #print(normscalar)
                return normscalar

        def Helper(tri, image, Colour = None):
            """Draws each rectangle for the _Draw function"""
            vec1 = Projection(tri[0], EVector = EVector, Orientation = Orientation)._int()
            vec2 = Projection(tri[1], EVector = EVector, Orientation = Orientation)._int()
            vec3 = Projection(tri[2], EVector = EVector, Orientation = Orientation)._int()
            """
            if EVector == None and Orientation == None:
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
            """
            try:
                NormValue = NormCalculator(tri)
                #print("computed", tri)
            except:
                #print(tri, "Could not compute")
                NormValue = 1
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
