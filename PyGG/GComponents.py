# Imports
import typing
from enum import IntEnum
from itertools import cycle
from threading import Timer

from . import (GError, GImage, GVector, GRectangle, GTexture)


# Classes
class GComponent:
    """Base class of game engine components, adds component_name attribute"""

    _DEFAULT_TAG = "default_tag"

    def __init__(self, component_name: str, component_tag: str = _DEFAULT_TAG):
        self._component_name = component_name
        self._component_tag = component_tag

    @property
    def component_name(self) -> str:
        """Returns component_name"""
        return self._component_name

    @property
    def component_tag(self) -> str:
        """Returns component_tag"""
        return self._component_tag


class GBoxCollider(GComponent):
    """Implements BoxCollider gameobject component, that is used to check intersections"""

    def __init__(self, component_name: str, *,
                 component_tag: str = GComponent._DEFAULT_TAG, box: GRectangle):
        super().__init__(component_name, component_tag)
        self.__box = box

    def move(self, vector: GVector):
        """Moves collider on vector by moving it's box rectangle on vector"""
        self.__box.move(vector)

    @property
    def collider(self):
        """Returns self.__box"""
        return self.__box


class GSprite(GComponent):
    """Implements sprite that can be placed on gameobject"""

    class Animation:
        """Implements animation for GSprite"""

        class __AnimationState(IntEnum):
            """Animation states"""
            DISABLED = 0
            ENABLED = 1

        def __init__(self, sprite,
                     images_dictionary: typing.Dict[str, typing.Iterable[GImage]]):
            self.binded_sprite = sprite
            self.packed_images = {key: cycle(value) for key, value in images_dictionary.items()}
            self.status: str = "idle"
            self.__animation_state = self.__AnimationState["DISABLED"]
            self.__timer: Timer = Timer(0, self.animate)
            self.__images_generator: typing.Generator = (_ for _ in ())  # Empty

        def start_animation(self, delay: float = 1):
            """Start animation cycle if possible"""
            if self.__animation_state == self.__AnimationState["ENABLED"]:
                raise GError("Failed to start animation, cause it was already enabled")
            self.__animation_state = self.__animation_state["ENABLED"]
            self.__images_generator = self.generator()
            self.animate(delay)

        def animate(self, delay: float):
            """Function that is called every animation cycle iteration"""
            if self.__animation_state == self.__AnimationState["ENABLED"]:
                self.binded_sprite.set_image(next(self.__images_generator))
                self.__timer = Timer(delay, self.animate)
                self.__timer.start()

        def stop_animation(self):
            """Stops animation cycle if possible"""
            if self.__animation_state == self.__AnimationState["DISABLED"]:
                raise GError("Failed to stop animation, cause it wasn't enabled")
            self.__timer.cancel()

        def generator(self):
            """Creates generator of images"""
            while True:
                if self.__animation_state == self.__AnimationState["ENABLED"]:
                    yield self.packed_images[self.status].next()

    def __init__(self, component_name: str, *,
                 component_tag: str = GComponent._DEFAULT_TAG, texture: GTexture):
        super().__init__(component_name, component_tag)
        self.texture = texture
        self.__animation: GSprite.Animation = self.Animation(self, {})

    def bind_animation(self, images_dictionary: typing.Dict[str, typing.Iterable[GImage]]):
        """Binds animation to sprite"""
        self.__animation = self.Animation(self, images_dictionary)

    def move(self, vector: GVector):
        """Moves sprite on vector"""
        self.texture.move(vector)

    def set_image(self, image: GImage):
        """Sets image to binded window image"""
        self.texture.set_image(image)

    def render(self):
        """Shows itself on window"""
        self.texture.render()

    @property
    def binded_animation(self):
        """Returns self.__animation"""
        return self.__animation

