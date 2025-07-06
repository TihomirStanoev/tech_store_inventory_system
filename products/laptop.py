from products.electronics import Electronics
from features.battery_powered import BatteryPowered
from features.mixin import CapacityMixin


class Laptop(Electronics, BatteryPowered, CapacityMixin):
    """
    Represents a laptop, inheriting from Electronics, BatteryPowered, and CapacityMixin.
    This class demonstrates multiple inheritance.
    """
    def __init__(self, name:str, price:int, battery_capacity_mah:int, processor:str, ram:int):
        """
        Initializes a Laptop instance.

        Note on multiple inheritance initialization:
        - super().__init__() calls the __init__ of the next class in the Method Resolution Order (MRO),
          which is Electronics -> Product.
        - BatteryPowered.__init__() is called explicitly because it's a secondary base class (mixin)
          and its __init__ needs to be triggered separately.

        :param name: The name of the laptop.
        :param price: The price of the laptop.
        :param battery_capacity_mah: The battery capacity in mAh.
        :param processor: The type of the processor.
        :param ram: The amount of RAM in GB.
        """
        super().__init__(name, price) # Correctly initializes Electronics -> Product chain
        BatteryPowered.__init__(self, battery_capacity_mah)
        self.processor = processor
        self.ram = ram


    @property
    def ram(self) -> int:
        """Gets the amount of RAM in GB."""
        return self.__ram 

    @ram.setter
    def ram(self, value) -> None:
        """Sets the RAM size with validation against allowed values."""  
        if not isinstance(value, int):
            raise ValueError('RAM must be a numeric value.')
        if value not in self.RAM_CAPACITY:
            raise ValueError(f'Invalid RAM size. Must be one of {", ".join(str(gb) for gb in self.RAM_CAPACITY)} GB')
        self.__ram = value


    @property
    def processor(self) -> str:
        """Gets the processor type."""
        return self.__processor

    @processor.setter 
    def processor(self, value) -> None:
        """Sets the processor type."""
        if not value:
            raise ValueError('The processor name cannot be an empty string.')
        self.__processor = str(value)
    

    def upgrade_ram(self, additional_ram):
        """
        Upgrades the RAM to a new, larger size.

        :param new_ram_size: The new total size of the RAM.
        :return: True if the upgrade was successful, False otherwise.
        """
        if additional_ram > self.__ram:
            self.ram = additional_ram


    def get_details(self):
        """
        Overrides the parent method to include all laptop-specific details.

        :return: A formatted string with all product details.
        """
        electronics_details = super().get_details()
        return f'{electronics_details}, Processor: {self.__processor}, RAM: {self.__ram} GB'

