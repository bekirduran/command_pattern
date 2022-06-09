from command_pattern.Commands import Maintenance
from command_pattern.EnumList import MaintenanceType


class MaintenanceFactory:

    @staticmethod
    def execute(maintenance: Maintenance, maintenance_type: MaintenanceType):
        maintenance.execute_maintenance(maintenance_type)

