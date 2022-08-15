from __future__ import annotations
from abc import ABC, abstractmethod


class Serviceable(ABC):
    """
    The Serviceable class declares the factory method that is supposed to return the
    status of whether the object is serviceable or not using the specific condition
    """

    @abstractmethod
    def needs_service(self):
        """
        The method determining the specific object is on service or not using the
        condition giving
        """
        pass
