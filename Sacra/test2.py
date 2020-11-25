from Renderer import Renderer2 as re
import SacraMathEngine as me
import os

#Creating an octahedron
Object = me.MeshObject3d()
Object += me.Triangle(me.vec3d(0,0,0), me.vec3d(1,0,0), me.vec3d(1,0,1))
Object += me.Triangle(me.vec3d(1,0,1), me.vec3d(0,0,1), me.vec3d(0,0,0))
Object += me.Triangle(me.vec3d(0,0,0), me.vec3d(1,0,0), me.vec3d(1,1,-1))
Object += me.Triangle(me.vec3d(1,1,-1), me.vec3d(0,0,1), me.vec3d(0,0,0))
Object += me.Triangle(me.vec3d(0,0,0), me.vec3d(0,0,1), me.vec3d(-1,1,1))
Object += me.Triangle(me.vec3d(-1,1,1), me.vec3d(-1,1,0), me.vec3d(0,0,0))
Object += me.Triangle(me.vec3d(1,0,0), me.vec3d(1,1,0), me.vec3d(1,1,1))
Object += me.Triangle(me.vec3d(1,1,1), me.vec3d(1,0,1), me.vec3d(1,0,0))
object2 = re(Object)._Draw(Frame = "octahedron")
