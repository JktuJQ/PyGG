# Imports
import typing

from . import (GBoxCollider, GSprite, GGameObject, GScene)


# Classes
class GGameProcessor:
    """Processes all game data such as events, collisions and etc."""

    @staticmethod
    def process(scene: GScene):
        """Main process"""
        gameobjects = scene.gameobjects
        sprites: typing.List[GSprite] = list()
        colliders: typing.Dict[GGameObject, typing.List[GBoxCollider]] = dict()
        for gameobject in gameobjects:
            for component in gameobject.components.values():
                if issubclass(type(component), GSprite):
                    sprites.append(component)
                if issubclass(type(component), GBoxCollider):
                    if component not in colliders.values():
                        colliders[gameobject] = [component]
                    else:
                        colliders[gameobject].append(component)

        # Render
        for sprite in sprites:
            sprite.render()

        # Checking collision
        for gameobject1 in colliders.keys():
            for gameobject2 in colliders.keys():
                if gameobject1 == gameobject2:
                    continue
                for collider1 in colliders[gameobject1]:
                    for collider2 in colliders[gameobject2]:
                        if collider1.collider.intersects_with(collider2.collider):
                            gameobject1.event_handler["on_collision"].signal(gameobject1, gameobject2)
                            gameobject2.event_handler["on_collision"].signal(gameobject2, gameobject1)
