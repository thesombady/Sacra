import os
import sys
from concurrent.futures import ProcessPoolExecutor


class PlaySound:
    def __init__(self):
        self.Generalpath = '/Users/andreasevensen/Documents/GitHub/Sacra/Audio/AudioFiles/' # Change location settings

    def Play(self, NameOfFile):
        path = os.path.join(self.Generalpath, NameOfFile)
        os.system(f'afplay {path}')

LoginSound = PlaySound().Play('Exodus.mp3')
