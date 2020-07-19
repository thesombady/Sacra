try:
    from SacraMathEngine import *
except:
    raise ImportError("Cannot import SacraMathEngine.")

class Lightsource:

    def __init__(self, vec):
        self.vec = vec

    def LightingAngle(self, Triangle):
        """Compute the angle of which the triangle plane is facing."""
        pass
