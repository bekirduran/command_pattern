from command_pattern.EnumList import MaintenanceType
from command_pattern.Commands.Maintenance import Maintenance


class MercedesMaintenance(Maintenance):

    def execute_maintenance(self,maintenance: MaintenanceType) -> None:
        print(":::.Mercedes Maintenance is Starting.:::")
        print(f"...your selection is : {maintenance.name}")
        print("maintenance is over GoodBye")
