from command_pattern.Commands.AudiMaintenance import AudiMaintenance
from command_pattern.Commands.BMWMaintenance import BMWMaintenance
from command_pattern.EnumList import MaintenanceType
from command_pattern.MaintenanceFactory import MaintenanceFactory
from command_pattern.Commands.MercedesMaintenance import MercedesMaintenance


if __name__ == "__main__":
    maintenance_room = MercedesMaintenance()
    MaintenanceFactory.execute(maintenance_room, MaintenanceType.standard_package)

    print("------------------------------------------------------")
    maintenance_room = AudiMaintenance()
    MaintenanceFactory.execute(maintenance_room, MaintenanceType.advanced_package)

    print("------------------------------------------------------")
    maintenance_room = BMWMaintenance()
    MaintenanceFactory.execute(BMWMaintenance(), MaintenanceType.special_package)
