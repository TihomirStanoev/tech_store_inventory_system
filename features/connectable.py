class Connectable:
    """
    A mixin class for devices that have network connectivity capabilities,
    like Bluetooth and Wi-Fi.
    """
    BLUETOOTH_VERSIONS = {
        "1.2": "1 Mbps",
        "2.0": "3 Mbps",
        "2.1": "3 Mbps",
        "3.0": "24 Mbps",
        "4.0": "24 Mbps",
        "4.1": "24 Mbps",
        "4.2": "24 Mbps",
        "5.0": "50 Mbps",
        "5.1": "50 Mbps",
        "5.2": "50 Mbps",
        "5.3": "50 Mbps",
        "5.4": "50 Mbps",
    }   
    WIFI_STANDARDS = {
        "802.11a": "54 Mbps",
        "802.11b": "11 Mbps",
        "802.11g": "54 Mbps",
        "802.11n": "600 Mbps",
        "802.11ac": "6.9 Gbps",
        "802.11ax": "9.6 Gbps",
        "802.11be": "46 Gbps", 
    }


    def __init__(self, bluetooth_version:str, wifi_standard:str):
        """
        Initializes a Connectable instance.

        :param bluetooth_version: The version of Bluetooth supported.
        :param wifi_standard: The Wi-Fi standard supported.
        """
        self.bluetooth_version = bluetooth_version
        self.wifi_standard = wifi_standard
        self.__is_connected = False
        self.wifi_name = None
    
    @property
    def bluetooth_version(self) -> str:
        """Gets the Bluetooth version and its corresponding speed in a formatted string."""
        key = self.__bluetooth_version
        value = Connectable.BLUETOOTH_VERSIONS[self.__bluetooth_version]
        return f'{key}: {value}'
    
    @bluetooth_version.setter
    def bluetooth_version(self, value:str):
        """Sets the Bluetooth version with validation."""
        string_value = str(value)
        if string_value not in Connectable.BLUETOOTH_VERSIONS:
            raise ValueError('Invalid bluetooth version.')
        self.__bluetooth_version = string_value
    

    @property
    def wifi_standard(self) -> str:
        """Gets the Wi-Fi standard and its corresponding speed in a formatted string."""
        key = self.__wifi_standard
        value = Connectable.WIFI_STANDARDS[self.__wifi_standard]
        return f'{key}: {value}'
    

    @wifi_standard.setter
    def wifi_standard(self, value:str) -> None:
        """Sets the Wi-Fi standard with validation."""
        string_value = str(value)
        if string_value not in Connectable.WIFI_STANDARDS:
            raise ValueError('Invalid Wi-Fi version.')
        self.__wifi_standard = string_value

    def connect_to_wifi(self, name:str) -> None:
        """Connects the device to a Wi-Fi network."""
        self.__is_connected = True
        self.wifi_name = name


    def disconnect(self) -> None:
        """Disconnects the device from the Wi-Fi network."""
        self.__is_connected = False
    

    def get_connection_info(self) -> str:
        """Returns a string with the current connection status."""
        if self.__is_connected:
            return f'Connected to wi-fi {self.wifi_name}'
        return f'Not connected!'