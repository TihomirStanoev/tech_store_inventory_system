class BatteryPowered:
    """
    Representing devices that are powered by a battery.
    Provides functionality for charging, usage, and status monitoring.
    """
    BATTERY_FULLY_CHAGRE = 100 # Corrected spelling

    def __init__(self, battery_capacity_mah:int):
        """
        Initializes a BatteryPowered instance.

        :param battery_capacity_mah: The total capacity of the battery in mAh.
        """
        self.battery_capacity_mah = battery_capacity_mah
        self.__current_charge_percentage = BatteryPowered.BATTERY_FULLY_CHAGRE
 

    @property
    def current_charge_percentage(self) -> int:
        """Gets the current battery charge percentage."""
        return self.__current_charge_percentage


    @property
    def battery_capacity_mah(self) -> int:
        """Gets the total capacity of the battery."""
        return self.__battery_capacity_mah

    @battery_capacity_mah.setter
    def battery_capacity_mah(self, value:int):
        """Sets the battery capacity with validation."""
        if not isinstance(value, int):
            raise ValueError('Battery capacity must be a integer value.')
        if value <= 0:
            raise ValueError('Battery capacity must be a positive number.')
        self.__battery_capacity_mah = value



    def charge(self) -> None:
        """Fully charges the battery to 100%."""
        self.__current_charge_percentage = BatteryPowered.BATTERY_FULLY_CHAGRE


    def use_device(self, hours:int, power:int) -> int:
        """
        Simulates using the device for a certain number of hours, consuming power.
        Updates the battery percentage.
        returns a negative number representing the time deficit in hours.
        """ 
        required_energy = power * hours
        available_energy = self.__battery_capacity_mah * (self.__current_charge_percentage / 100)

        if required_energy > available_energy:    
            self.__current_charge_percentage = 0    
            return (available_energy / power) - hours

        battery_consumption = available_energy - (power * hours) 
        self.__current_charge_percentage = int((battery_consumption / self.__battery_capacity_mah) * 100)
        return hours


