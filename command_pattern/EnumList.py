from enum import Enum


class CarType(Enum):
    Mercedes = 1
    BMW = 2
    Audi = 3
    Renault = 4


class MaintenanceType(Enum):
    standard_package = 1
    advanced_package = 2
    special_package = 3
