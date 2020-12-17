"""
PyGG - simple written in Python game engine compatible with Python GUI libraries such as
tkinter, pygame turned into wrapper classes

The main purpose of this game engine - make developing 2D games on Python easier,
applying different classes. Architecture of PyGG is similar to Unity architecture,
it is based on GGameObjects, the functionality of which is implemented by the GComponents.

---------------------------------------------------------------------------------------------------

This python package was created at 15.07.20
"""

from .GErrors import *
from .GData import *
from .GCore import *
from .GEventSystem import *
from .GComponents import *
from .GGameObjects import *
from .GSceneSystem import *
from .GGameProcessor import *
