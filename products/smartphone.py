from products.electronics import Electronics
from features.connectable import Connectable
from features.battery_powered import BatteryPowered



class Smartphone(Electronics, Connectable, BatteryPowered):
    """
    Represents a smartphone, a complex device inheriting from Electronics,
    Connectable, and BatteryPowered.
    """
    def __init__(self, name:str, price:int|float, bluetooth_version:str, wifi_standard:str, battery_capacity_mah:int, screen_size:float, camera_megapixels:int):
        """
        Initializes a Smartphone instance.

        :param name: The name of the smartphone.
        :param price: The price of the smartphone.
        :param bluetooth_version: The supported Bluetooth version.
        :param wifi_standard: The supported Wi-Fi standard.
        :param battery_capacity_mah: The battery capacity in mAh.
        :param screen_size: The diagonal screen size in inches.
        :param camera_megapixels: The resolution of the main camera in megapixels.
        """
        super().__init__(name, price)
        Connectable.__init__(self, bluetooth_version, wifi_standard)
        BatteryPowered.__init__(self, battery_capacity_mah)
        self.screen_size = screen_size
        self.__camera_megapixels = camera_megapixels
    

    @property 
    def screen_size(self) -> float:
        """Gets the screen size in inches."""
        return self.__screen_size

    @screen_size.setter
    def screen_size(self, value:float):
        """Sets the screen size with validation."""
        if not isinstance(value, (float,int)):
            raise ValueError('The display size must be a numeric value.')
        self.__screen_size = value

    @property
    def camera_megapixels(self) -> int:
        """Gets the camera resolution in megapixels."""
        return self.__camera_megapixels

    @camera_megapixels.setter
    def camera_megapixels(self, value:int):
        """Sets the camera resolution with validation."""
        if not isinstance(value, (int)):
            raise ValueError('Resolution must be a numeric value.')
        self.__camera_megapixels = value


    def take_photo(self) -> str:
        """Simulates taking a photo with the smartphone's camera."""
        return f"{self.name} make photo with {self.__camera_megapixels} MPx camera!"
    
    def get_details(self) -> str:
        """
        Overrides the parent method to include all smartphone-specific details.

        :return: A formatted string with all product details.
        """
        electornics_details = super().get_details()
        return f'{electornics_details}, Screen Size: {self.__screen_size:.1f}, Camera: {self.__camera_megapixels}MPX'


