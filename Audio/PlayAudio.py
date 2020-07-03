import os
import sys
from concurrent.futures import ProcessPoolExecutor

def Hello():
    print('Hello')

def PlayLoginSound():
    os.system('afplay /Users/andreasevensen/Documents/GitHub/Sacra/Audio/AudioFiles/Exodus.mp3')

with ProcessPoolExecutor() as exector:
    future1 = exector.submit(PlayLoginSound)
    future2 = exector.submit(Hello)
