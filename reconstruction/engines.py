from abc import ABC


class Engine(ABC):
    """
    The class determining the engine used on the specific car
    """

    def needs_service(self) -> bool:
        """
        The function determining whether the engine needs a service or not
        :return a boolean representing whether this engine needs a service or not
        """
        pass


class CapuletEngine(Engine):
    """
    The class representing the object of CapuletEngine.
    """
    def __init__(self, last_service_mileage, current_mileage):
        """
        The initiation of the CapuletEngine
        :param last_service_mileage: The last mileage that this engine could be used.
        :param current_mileage: The current mileage in the speculation
        """
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage > self.last_service_mileage


class WilloughbyEngine(Engine):
    """
    The class representing the object of WilloughbyEngine.
    """
    def __init__(self, last_service_mileage, current_mileage):
        """
        The initiation of the WilloughbyEngine
        :param last_service_mileage: The last mileage that this engine could be used.
        :param current_mileage: The current mileage in the speculation
        """
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage > self.last_service_mileage


class SternmanEngine(Engine):
    """
    The class representing the object of SternmanEngine.
    """
    def __init__(self, warning_light_on):
        """
        The initiation of the SternmanEngine
        :param warning_light_on : The boolean representing whether the warning light is on or not
        """
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
