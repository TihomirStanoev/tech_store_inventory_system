class Product:
    """
    The base class for all products in the inventory system.
    Handles basic attributes like name, price, and a unique ID.
    """
    _ID = -1 # Class attribute to generate unique IDs
    MAX_DISCOUNT_PERCENTAGE = 50

    def __init__(self, name:str, price:int|float):
        """
        Initializes a Product instance.

        :param name: The name of the product.
        :param price: The initial price of the product.
        """
        self.price_history = []
        self.name = name
        self.price = price       
        Product._ID += 1
        self.__product_id = Product._ID
        


    @property
    def name(self) -> str:
        """Gets the name of the product."""
        return self.__name

    @name.setter
    def name(self, value:str) -> None:
        """Sets the product's name with validation."""
        if not value:
            raise ValueError('The name must contain at least one character!')
        self.__name = value

    @property
    def price(self) -> float:
        """Gets the current price of the product."""
        return self.__price

    @price.setter
    def price(self, value:int|float) -> None:
        """
        Sets the product's price with validation.
        Also records the new price in the price history.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('Price must be a numeric value.')
        if value <= 0:
            raise ValueError('Price must be a positive value greater than 0.')

        self.__price = value
        self.price_history.append(value)
        
    @property
    def product_id(self) -> int:
        """Gets the unique ID of the product."""
        return self.__product_id
    

    def apply_discount(self, percentage:int|float) -> bool:
        """
        Applies a discount to the product's price.

        The new price is recorded in the price history.
        :param percentage: The discount percentage to apply.
        :return: True if the discount was applied successfully, False otherwise.
        """
        if not (percentage > 0 and percentage <= Product.MAX_DISCOUNT_PERCENTAGE):
            return False

        self.__price *= (1 - percentage / 100)
        return True


    def get_details(self) -> str:
        """
        Gets a formatted string with the basic details of the product.
        """
        return f'ID: {self.__product_id}, Name: {self.__name}, Price: {self.__price:.2f}$'

