# Imports
import typing

from . import (GComponent, GEvent, GEventHandler)


# GGameObjects
class GGameObject:
    """GameObject class that handles objects components and implements slots for game signals"""

    DEFAULT_TAG = "default_tag"

    def __init__(self, gameobject_name: str, gameobject_tag: str = DEFAULT_TAG):
        self.__gameobject_name = gameobject_name
        self.__gameobject_tag = gameobject_tag
        self.__components: typing.Dict[str, GComponent] = dict()
        # Events
        self.__events = GEventHandler()
        self.__events.add_event("on_collision", GEvent(), default=True)

    def add_component(self, component: GComponent):
        """Adds component to game object"""
        self.__components[component.component_name] = component

    def remove_component(self, component_name: str):
        """Removes component from game object"""
        del self.__components[component_name]

    def get_component(self, component_name: str):
        """Returns component with the same name and if there is no returns None"""
        return self.__components[component_name]

    @property
    def gameobject_name(self):
        """Returns self.__gameobject_name"""
        return self.__gameobject_name

    @property
    def gameobject_tag(self):
        """Returns self.__gameobject_tag"""
        return self.__gameobject_tag

    @property
    def components(self):
        """Returns self.__components"""
        return self.__components

    @property
    def event_handler(self):
        """Returns self.__events"""
        return self.__events


