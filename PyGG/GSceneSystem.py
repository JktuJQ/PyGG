# Imports
import typing

from . import GGameObject


# Classes
class GScene:
    """Handles all game objects on scene"""

    def __init__(self, scene_name: str):
        self.__scene_name = scene_name
        self.__gameobjects: typing.List[GGameObject] = list()

    def add_gameobject(self, gameobject: GGameObject):
        """Adds gameobject to self.gameobjects and returns its index"""
        self.__gameobjects.append(gameobject)
        return len(self.__gameobjects) - 1

    def remove_gameobject(self, index: int):
        """Removes gameobject or group at index"""
        del self.__gameobjects[index]

    def get_gameobject(self, index: int):
        """Returns gameobject at index, if there is gameobject group - returns None"""
        return self.__gameobjects[index]

    @property
    def gameobjects(self):
        """Returns self.__gameobjects"""
        return self.__gameobjects.copy()

    @property
    def scene_name(self):
        """Returns self.__scene_name"""
        return self.__scene_name


class GSceneManager:
    """GSceneManager stores the data needed to create the scene"""

    def __init__(self):
        self.__scenes: typing.Dict[str, GScene] = dict()

    def add_scene(self, scene: GScene):
        """Adds scene to scene manager"""
        self.__scenes[scene.scene_name] = scene

    def remove_scene(self, scene_name: str):
        """Removes scene with the same name from scene manager"""
        del self.__scenes[scene_name]

    def get_scene(self, scene_name: str):
        """Returns scene with the same name"""
        return self.__scenes[scene_name]

    @property
    def scenes(self):
        """Returns self.__scenes"""
        return self.__scenes.copy()
