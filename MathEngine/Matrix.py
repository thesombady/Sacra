from Vector import Vec2d, Vec3d

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

class Matrix3d:

    def __init__(self, x1, x2, x3, y1, y2, y3, z1, z2, z3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.col1 = (self.x1, self.y1, self.z1)
        self.col2 = (self.x2, self.y2, self.z2)
        self.col3 = (self.x3, self.y3, self.z3)

    def __str__(self):
        return f'[({self.x1}, {self.x2}, {self.x3})\n ({self.y1}, {self.y2}, {self.y3})\n ({self.z1}, {self.z2}, {self.z3})]'

    def __add__(self, other):
        return Matrix3d(self.x1 + other.x1, self.x2 + other.x2, self.x3 + other.x3, self.y1 + other.y1, self.y2 + other.y2, self.y3 + other.y3,
        self.z1 + other.z1, self.z2 + other.z2, self.z3 + other.z3)

    def __mul__(self, other):
        if isinstance(other, Matrix3d):
            nx1 = self.x1 * other.x1 + self.x2 * other.y1 + self.x3 * other.z1
            nx2 = self.x1 * other.x2 + self.x2 * other.y2 + self.x3 * other.z2
            nx3 = self.x1 * other.x3 + self.x2 * other.y3 + self.x3 * other.y3
            ny1 = self.y1 * other.x1 + self.y2 * other.y1 + self.y3 * other.z1
            ny2 = self.y1 * other.x2 + self.y2 * other.y2 + self.y3 * other.z2
            ny3 = self.y1 * other.x3 + self.y2 * other.y3 + self.y3 * other.z3
            nz1 = self.z1 * other.x1 + self.z2 * other.y1 + self.z3 * other.z1
            nz2 = self.z1 * other.x2 + self.z2 * other.y2 + self.z3 * other.z2
            nz3 = self.z1 * other.x3 + self.z2 * other.y3 + self.z3 * other.z3
            return Matrix3d(nx1, nx2, nx3, ny1, ny2, ny3, nz1, nz2, nz3)
        else:
            return self.vecmul(other)

    def vecmul(self, vector):
        vec1 = self.x1 * vector[0] + self.x2 * vector[1] + self.x3 * vector[2]
        vec2 = self.y1 * vector[0] + self.y2 * vector[1] + self.y3 * vector[2]
        vec3 = self.z1 * vector[0] + self.z2 * vector[1] + self.z3 * vector[2]
        return Vec3d(vec1, vec2, vec3)
#unit = Matrix2d(1,0,0,1)
#vec1 = Vec2d(1,1)
#print(unit.vecmul(vec1))
unit = Matrix3d(1,0,0,0,1,0,0,0,1)
