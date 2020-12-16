# Imports
import typing

from . import GError


# Classes
class GEvent:
    """Implements event that can be generated as a signal and than be processed by slot"""

    def __init__(self):
        self.slots = list()

    def add_slot(self, function: typing.Callable):
        """Adds slot to event"""
        self.slots.append(function)

    def remove_slot(self, index: int):
        """Removes slot from event"""
        del self.slots[index]

    def signal(self, this: object, sender: object):
        """Invokes all event slots"""
        for function in self.slots:
            function(this, sender)


class GEventHandler:
    """Handles events of object"""

    def __getitem__(self, event_name: str):
        """Returns event with the same name"""
        for key in self.__events.keys():
            if event_name in key:
                return self.__events[key]
        raise GError("There is no event with the same name")

    def __init__(self):
        self.__events: typing.Dict[frozenset, GEvent] = dict()

    def add_event(self, event_name: str, event: GEvent, default=False):
        """
        Adds event to event handler
        If default is True, event becomes not removable by user
        """
        for key in self.__events.keys():
            if event_name in key:
                raise GError("This event name was already used")
        data = {event_name}
        if default:
            data.add("d")
        self.__events[frozenset(data)] = event

    def remove_event(self, event_name: str):
        """Removes event from event handler"""
        for key in self.__events.keys():
            if event_name in key:
                if "d" in key:
                    raise GError("This event marked as default, which means it cannot be removed")
                del self.__events[key]

    @property
    def events(self):
        """Returns self.__events"""
        return self.__events
