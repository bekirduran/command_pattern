from abc import ABC, abstractmethod

from command_pattern.EnumList import MaintenanceType


# this is my command class
class Maintenance(ABC):

    @abstractmethod
    def execute_maintenance(self, maintenance: MaintenanceType) -> None:
        pass
