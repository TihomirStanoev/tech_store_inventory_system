from products.electronics import Electronics
from features.mixin import CapacityMixin


class GamingConsole(Electronics, CapacityMixin):
    """
    Represents a gaming console, inheriting from Electronics and using CapacityMixin.
    Adds specific attributes like controller type and storage.
    """
    def __init__(self, name:str, price:int|float, controller_type:str, storage_gb:int):
        """
        Initializes a GamingConsole instance.

        :param name: The name of the console.
        :param price: The price of the console.
        :param controller_type: The type of controller included.
        :param storage_gb: The internal storage capacity in GB.
        """
        super().__init__(name, price)
        self.controller_type = controller_type
        self.storage_gb = storage_gb


    @property
    def storage_gb(self) -> int:
        """Gets the storage capacity in GB."""
        return self.__storage_gb

    @storage_gb.setter
    def storage_gb(self, value:int):
        """Sets the storage capacity with validation against allowed values."""
        if not isinstance(value, int):
            raise ValueError('Capacity must be a numeric value.')
        if value not in self.STORAGE_CAPACITY:
            raise ValueError(f'Capacity must be a value from the range {", ".join(str(gb) for gb in self.STORAGE_CAPACITY)} GB')
        self.__storage_gb = value

    @property
    def controller_type(self) -> str:
        """Gets the controller type."""
        return self.__controller_type

    @controller_type.setter
    def controller_type(self, value:str) -> None:
        """Sets the controller type."""
        if not value:
            raise ValueError('The controller type cannot be an empty string.')
        self.__controller_type = str(value)

    def pair_new_controller(self, new_controller_type:str) -> None:
        """Updates the controller type to a new one."""
        self.controller_type = new_controller_type


    def play_game(self, game_name:str) -> str:
        """
        Simulates playing a game on the console.

        :param game_name: The name of the game to be played.
        :return: A string describing the action.
        """
        return f'{game_name} played on {self.name} with {self.__controller_type} controller!'


    def get_details(self) -> str:
        """
        Overrides the parent method to include console-specific details.
        """
        electronics_details = super().get_details()
        return f'{electronics_details}, Controller: {self.__controller_type}, Storage: {self.__storage_gb}GB'


