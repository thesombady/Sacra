

class BuildWorld:
    """ A terrain Builder, refers to Perlin-noise. """

    def __init__(self, PerlinNoise = True):
        if PerlinNoise == False:
            pass
        else:
            self.PerlinNoise = PerlinNoise($0)
        pass
