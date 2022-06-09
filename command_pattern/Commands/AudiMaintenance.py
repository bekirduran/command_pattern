from command_pattern.EnumList import MaintenanceType
from command_pattern.Commands.Maintenance import Maintenance


class AudiMaintenance(Maintenance):

    def execute_maintenance(self, maintenance: MaintenanceType):
        print(":::.Audi Maintenance is Starting.:::")
        print("Some differences about audi maintenance")
        print(f"...your selection is : {maintenance.name}")
        print("maintenance is over GoodBye")
