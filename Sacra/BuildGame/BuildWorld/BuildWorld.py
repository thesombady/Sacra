from random import randint

class BuildWorld:
    """ A terrain Builder, refers to Perlin-noise. """

    def __init__(self, Size, PerlinNoise = True):
        if PerlinNoise == False:
            pass
        else:
            self.PerlinNoise = PerlinNoise
        if len(Size) < 3:
            raise KeyError("The size of the world has to be three-dimensional-object which describes the different axis.")
        else:
            self.Size = Size
        if self.PerlinNoise == True:
            self.BuildTerrainPer()
        else:
            self.BuildTerrainNotPer()

    def BuildTerrainPer(self):
        pass

    def BuildTerrainNotPer(self):
        pass
