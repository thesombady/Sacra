
class Vec3d:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (self.x, self.y, self.z)

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def __add__(self, other):
        return Vec3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __getitem__(self, index):
        return self.vector[index]
    """
    def __mul__(self, scalar):
        return Vec3d(self.x * scalar, self.y * scalar, self.z * scalar)
    """
    """
    def __mul__(self, other):
        return Vec3d(self.x * (other.x + other.y + other.z), self.y * (other.x + other.y + other.z), self.z * (other.x + other.y + other.z)
    """

    def __rmul__(self, scalar):
        return Vec3d(self.x * scalar, self.y * scalar, self.z * scalar)


    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)




class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = (self.x, self.y)

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2d(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vec2d(self.x * scalar, self.y * scalar)


    def __getitem__(self, index):
        return self.vector[index]


    def dot(self, other):
        return (self.x * other.x + self.y * other.y)

    def cross(self, other):
        return None #Implement cross product definition

    def norm(self):
        return (self.x ** 2 + self.y ** 2)**(1/2)

    def normalize(self):
        return 1 / self.norm() * self
