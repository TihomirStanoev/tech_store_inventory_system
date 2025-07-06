from datetime import date
from dateutil.relativedelta import relativedelta
from products.product import Product


class Electronics(Product):
    """
    Represents an electronic product, inheriting from Product.
    Adds functionality related to warranty and purchase date.
    """
    WARRANTY_PERIOD = 24 # Default warranty period in months

    def __init__(self, name:str, price:int|float):
        """Initializes an Electronics instance."""
        super().__init__(name, price)
        self.__warranty_period = Electronics.WARRANTY_PERIOD
        self.__purchase_date = None


    def buy(self) -> None:
        """
        Sets the purchase date to the current date, simulating a purchase.
        This action starts the warranty period.
        """
        self.__purchase_date = date.today()
    

    def is_warranty_active(self) -> bool:
        """
        Checks if the product's warranty is still active.

        :return: True if the warranty is active, False if it has expired
                 or if the product has not been purchased yet.
        """
        if self.__purchase_date is None:
            return False
        warranty_expiration = self.__purchase_date + relativedelta(months = self.__warranty_period)
        return date.today() <= warranty_expiration


    def get_details(self) -> str:
        """
        Overrides the parent method to include warranty information in the details.

        :return: A formatted string with product details including warranty.
        """
        product_details = super().get_details()
        return f'{product_details}, Warranty: {self.__warranty_period} months'

