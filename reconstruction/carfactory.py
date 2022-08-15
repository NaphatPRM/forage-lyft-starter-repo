from abc import ABC
from car import Car
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery


class CarFactory(ABC):
    """
    + create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    + create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    + create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): Car
    + create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    + create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    """

    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        """
        A method used for creating a new calliope car object
        :param current_date: The date when the function is called
        :param last_service_date: The last date that this Calliope car can be on service
        :param current_mileage: The current amount of mileage of this car
        :param last_service_mileage: The threshold amount of the mileage before the service
        :return: The calliope car object with the specific characteristics
        """
        calliope_engine = CapuletEngine(last_service_mileage, current_mileage)
        calliope_battery = SpindlerBattery(last_service_date, current_date)
        calliope_car = Car(calliope_engine, calliope_battery)
        return calliope_car

    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        """
        A method used for creating a new glissade car object
        :param current_date: The date when the function is called
        :param last_service_date: The last date that this Glissade car can be on service
        :param current_mileage: The current amount of mileage of this car
        :param last_service_mileage: The threshold amount of the mileage before the service
        :return:
        """
        glissade_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        glissade_battery = SpindlerBattery(last_service_date, current_date)
        glissade_car = Car(glissade_engine, glissade_battery)
        return glissade_car

    def create_palindrome(self, current_date, last_service_date, warning_light_on: bool):
        """
        A method used for creating a new palindrome car object
        :param current_date: The date when the function is called
        :param last_service_date: The last date that this Palindrome car can be on service
        :param warning_light_on:
        :return:
        """
        palindrome_engine = SternmanEngine(warning_light_on)
        palindrome_battery = SpindlerBattery(last_service_date, current_date)
        palindrome_car = Car(palindrome_engine, palindrome_battery)
        return palindrome_car

    def create_rorschach(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        """
        A method used for creating a new rorschach car object
        :param current_date: The date when the function is called
        :param last_service_date: The last date that this Rorschach car can be on service
        :param current_mileage: The current amount of mileage of this car
        :param last_service_mileage: The threshold amount of the mileage before the service
        :return:
        """
        rorschach_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        rorschach_battery = NubbinBattery(last_service_date, current_date)
        rorschach_car = Car(rorschach_engine, rorschach_battery)
        return rorschach_car

    def create_thovex(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        """
        A method used for creating a new thovex car object
        :param current_date: The date when the function is called
        :param last_service_date: The last date that this Thovex car can be on service
        :param current_mileage: The current amount of mileage of this car
        :param last_service_mileage: The threshold amount of the mileage before the service
        :return:
        """
        thovex_engine = CapuletEngine(last_service_mileage, current_mileage)
        thovex_battery = NubbinBattery(last_service_date, current_date)
        thovex_car = Car(thovex_engine, thovex_battery)
        return thovex_car
