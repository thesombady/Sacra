
class Vec3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, Vec3d):
            return Vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __radd__(self, other):
        if isinstance(other, Vec3d):
            return Vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, Vec3d):
            Vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __rsub__(self, other):
        if isinstance(other, Vec3d):
            Vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __mul__(self, value):
        if isinstance(value, (float, int)):
            return Vec3d(self.x * value, self.y * value, self.z * value)
        else:
            pass

    def __rmul__(self, value):
        if isinstance(value, (float, int)):
            return Vec3d(self.x * value, self.y * value, self.z * value)
        else:
            pass

    def __str__(self):
        return f'<({self.x}, {self.y}, {self.z})>'

    def __getitem__(self, index):
        return self.vector[index]

    def dot(self, other):
        if isinstance(other, Vec3d):
            value = self.x * other.x + self.y * other.y + self.z * other.z
        else:
            pass

    def cross(self, other):
        if isinstance(other, Vec3d):
            col1 = self.y * other.z - self.z * other.y
            col2 = self.z * other.x - self.x * other.z
            col3 = self.x * other.y - self.y * other.x
            return Vec3d(col1, col2, col3)
        else:
            pass
    def norm(self):
        value = (self.x ** 2 + self.y ** 2 + self.z **2) ** (0.5)
        return value

    def normalize(self):
        return 1/self.norm() * self


vec1 = Vec3d(1,1,1)
print(vec1.normalize())
