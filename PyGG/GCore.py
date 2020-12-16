# Imports
from dataclasses import dataclass

from . import GImage


# Classes
@dataclass
class GVector:
    """Implements 2D vector, that is used to move different objects from their positions"""

    def __neg__(self):
        """Returns GVector based on its own with negative offset_x and negative offset_y"""
        return GVector(-self.offset_x, -self.offset_y)

    def __invert__(self):
        """Returns GVector based on its own with offset_x and offset_y swapped"""
        return GVector(self.offset_y, self.offset_x)

    def __add__(self, other):
        return GVector(self.offset_x + other.offset_x, self.offset_y + other.offset_y)

    def __sub__(self, other):
        return GVector(self.offset_x - other.offset_x, self.offset_y - other.offset_y)

    offset_x: int
    offset_y: int


@dataclass
class GPoint:
    """Implements simple 2D point on surface with integer x and y, that can be moved on GVector"""

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        """Unpacks itself as a tuple of x and y"""
        return iter((self.x, self.y))

    x: int
    y: int

    def move(self, vector: GVector):
        """Moves point, adding to x and y vector offsets"""
        self.x += vector.offset_x
        self.y += vector.offset_y


class GRectangle:
    """Implements simple rectangle on surface"""

    def __init__(self, point_ul: GPoint, point_br: GPoint):
        self.point_ul = point_ul
        self.point_br = point_br

    def intersects_with(self, other_rectangle):
        if set(self.x_range) & set(other_rectangle.x_range) and set(self.y_range) & set(other_rectangle.y_range):
            return True
        else:
            return False

    def move(self, vector: GVector):
        self.point_ul.move(vector)
        self.point_br.move(vector)

    @property
    def x_range(self) -> range:
        return range(self.point_ul.x, self.point_br.x)

    @property
    def y_range(self) -> range:
        return range(self.point_ul.y, self.point_br.y)


    @classmethod
    def from_wh(cls, point_ul: GPoint, w: int, h: int):
        return cls(point_ul, GPoint(point_ul.x + w, point_ul.y + h))


class GTexture:
    """Interface of image on window that must be able to move, change image
       Must be inherited"""

    def move(self, vector: GVector):  # Must be overridden
        """Moves window image on vector"""
        pass

    def set_image(self, image: GImage):  # Must be overridden
        """Sets new image to window image"""
        pass

    def render(self):  # Must be overridden
        """Shows itself on window"""
        pass
