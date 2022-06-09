from command_pattern.EnumList import MaintenanceType
from command_pattern.Commands.Maintenance import Maintenance


class BMWMaintenance(Maintenance):

    def execute_maintenance(self, maintenance: MaintenanceType):
        print(":::.BMW Maintenance is Starting.:::")
        print("Some differences about BMW maintenance")
        print("BMW additional maintenance")
        print(f"...your selection is : {maintenance.name}")
        print("maintenance is over GoodBye")
