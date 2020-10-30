#Code will enter at later date.
from setuptools import setup, find_packages
with open("readme.md", 'r') as file:
    long_description = file.read()

setup(
    name = "Sacra Game Engine",
    author = "Andreas Evensen",
    version = "0.0.1"
    author_email = "andreas.evensen11@gmail.com",
    description = "Game Engine built untop of Tkinter",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    find_packages = find_packages(),
    License = "MIT",
    keywords = "GameEngine",
    install_requires = ["SacraMathEngine", "SacraPhysicsEngine"],
    python_requires = '>=3.6',
)
