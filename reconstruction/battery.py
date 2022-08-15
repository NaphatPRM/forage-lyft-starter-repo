from abc import ABC


class Battery(ABC):
    """
    The class determining the battery used on the specific car.
    """

    def needs_service(self) -> bool:
        """
        The function determining whether the battery needs a service or not.
        :return a boolean representing whether this battery needs a service or not.
        """
        pass


class SpindlerBattery(Battery):
    """
    The class representing the object of Spindler Battery.
    Alternative Idea : Instead of making the last_service_date to be on the field,
    making the first_service_date as a field and make the needs_service to be that date + used time
    which is determined in the first task
    """
    def __init__(self, last_service_date, current_date):
        """
        The initiation of the SpindlerBattery
        :param last_service_date: The last day that this battery can be serviced, which is 2 years
        :param current_date: The current date in the speculation
        """
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date > self.last_service_date


class NubbinBattery(Battery):
    """
    The class representing the object of Nubbin Battery.
    Alternative Idea : Instead of making the last_service_date to be on the field,
    making the first_service_date as a field and make the needs_service to be that date + used time
    which is determined in the first task
    """
    def __init__(self, last_service_date, current_date):
        """
        The initiation of the NubbinBattery
        :param last_service_date: The last day that this battery can be serviced, which is 2 years
        :param current_date: The current date in the speculation
        """
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date > self.last_service_date
