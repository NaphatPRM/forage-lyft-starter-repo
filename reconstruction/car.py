from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery):
        """
        The initiation of the object car
        :param engine: The engine used in this car
        :param battery: THe battery used in this car
        """
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() & self.battery.needs_service()
