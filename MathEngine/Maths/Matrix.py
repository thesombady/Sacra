from Vector import vec3d

class matrix3d:
    """ Intalizes a matrix which is in R^3 space; Of which the basic eigen-values can be computed. """
    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        self.matrix = (self.vec1, self.vec2, self.vec3)

    def __str__(self):
        return f'<({self.vec1[0]}, {self.vec1[1]}, {self.vec1[2]})\n ({self.vec2[0]}, {self.vec2[1]}, {self.vec2[2]})\n ({self.vec3[0]}, {self.vec3[1]}, {self.vec3[2]})>'

    def __add__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __radd__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __rsub__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return matrix3d(vec1 * other, vec2 * other, vec3 * other)
        elif isinstance(other, vec3d):
            col1 = self.vec1[0] * other[0] + self.vec1[1] * other[1] + self.vec1[2] * other[2]
            col2 = self.vec2[0] * other[0] + self.vec2[1] * other[1] + self.vec2[2] * other[2]
            col3 = self.vec3[0] * other[0] + self.vec3[1] * other[1] + self.vec3[2] * other[2]
            return vec3d(col1, col2, col3)
        elif isinstance(other, matrix3d):
            x1 = self.vec1[0] * other.vec1[0] + self.vec1[1] * other.vec2[0] + self.vec1[2] * other.vec3[0]
            x2 = self.vec1[0] * other.vec1[1] + self.vec1[1] * other.vec2[1] + self.vec1[2] * other.vec3[1]
            x3 = self.vec1[0] * other.vec1[2] + self.vec1[1] * other.vec2[2] + self.vec1[2] * other.vec3[2]
            nvec1 = vec3d(x1, x2, x3)
            y1 = self.vec2[0] * other.vec1[0] + self.vec2[1] * other.vec2[0] + self.vec2[2] * other.vec3[0]
            y2 = self.vec2[0] * other.vec1[1] + self.vec2[1] * other.vec2[1] + self.vec2[2] * other.vec3[1]
            y3 = self.vec2[0] * other.vec1[2] + self.vec2[1] * other.vec2[2] + self.vec2[2] * other.vec3[2]
            nvec2 = vec3d(y1, y2, y3)
            z1 = self.vec3[0] * other.vec1[0] + self.vec3[1] * other.vec2[0] + self.vec3[2] * other.vec3[0]
            z2 = self.vec3[0] * other.vec1[1] + self.vec3[1] * other.vec2[1] + self.vec3[2] * other.vec3[1]
            z3 = self.vec3[0] * other.vec1[2] + self.vec3[1] * other.vec2[2] + self.vec3[2] * other.vec3[2]
            nvec3 = vec3d(z1, z2, z3)
            return matrix3d(nvec1, nvec2, nvec3)
        else:
            pass

    def trace(self):
        return self.vec1[0] + self.vec2[1] + self.vec3[2]

class Matrix2d:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.col1 = (self.x1, self.y1)
        self.col2 = (self.x2, self.y2)

    def __str__(self):
        return f'[({self.x1}, {self.x2})\n ({self.y1}, {self.y2})]'

    def __add__(self, other):
        return Matrix2d(self.x1 + other.x1, self.x2 + other.x2, self.y1 + other.y1, self.y2 + other.y2)

    def __sub__(self, other):
        return Matrix2d(self.x1 - other.x1, self.x2 - other.x2, self.y1 - other.y1, self.y2 - other.y2)

    def __mul__(self, other):
        nx1 = self.x1 * other.x1 + self.x2 * other.y1
        nx2 = self.x1 * other.x2 + self.x2 * other.y2
        ny1 = self.y1 * other.x1 + self.y2 * other.y1
        ny2 = self.y1 * other.x2 + self.y2 * other.y2
        return Matrix2d(nx1, nx2, ny1, ny2)

    def vecmul(self, vector):
        vec1 = self.x1 * vector[0] + self.y1 * vector[1]
        vec2 = self.x2 * vector[0] + self.y2 * vector[1]
        return Vec2d(vec1, vec2)
