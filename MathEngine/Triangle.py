from Vector import Vec2d, Vec3d

class Triangle(Vec3d):
    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
