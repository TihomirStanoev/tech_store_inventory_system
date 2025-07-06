from products.electronics import Electronics
from features.battery_powered import BatteryPowered
from products.product import Product 

class Inventory:
    """
    Manages the collection of all products in a store.
    Handles adding, removing, finding, and reporting on products.
    """
    def __init__(self, name:str):
        """
        Initializes an Inventory instance.

        :param name: The name of the store or inventory.
        """
        self.name = name
        self.products = {}


    def add_product(self, product) -> bool:
        """
        Adds a product to the inventory.
        Prevents adding a product if an item with the same ID already exists.
        :return: True if the product was added successfully, False otherwise.
        """
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            return True
        return False
    

    def remove_product(self, product_id) -> bool:
        """
        Removes a product from the inventory by its ID.

        :param product_id: The ID of the product to remove.
        :return: True if the product was removed successfully, False otherwise.
        """
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def find_product(self, product_id) -> Product | None:
        """
        Finds and returns a product by its ID.

        :param product_id: The ID of the product to find.
        :return: The product object if found, otherwise None.
        """
        return self.products.get(product_id, None)


    def generate_stock_report(self) -> str:
        """
        Generates a detailed string report of all products in the inventory.

        :return: A multi-line string with details for each product.
        """
        return '\n'.join(prod.get_details() for prod in self.products.values())


    def get_out_of_warranty_electronics(self) -> list[Electronics]:
        """
        Filters and returns a list of all electronic products whose warranty has expired.

        :return: A list of Electronics objects that are out of warranty.
        """
        out_of_warranty = []

        for product in self.products.values():
            if isinstance(product, Electronics):
                if not product.is_warranty_active():
                    out_of_warranty.append(product)
        
        return out_of_warranty


    def calculate_total_stock_value(self) -> float:
        """
        Calculates the total monetary value of all products in the inventory.

        :return: The sum of the prices of all products.
        """
        return sum(product.price for product in self.products.values())

    
    def charge_all_devices(self) -> None:
        """
        Finds all devices with batteries in the inventory and charges them to full.
        """
        for product in self.products.values():
            if isinstance(product, BatteryPowered):
                product.charge()
    
    def get_products_by_name(self, name_query:str) -> list[Product]:
        """
        Finds all products whose name contains the given query string.

        :param name_query: The string to search for within product names.
        :return: A list of product objects that match the query.
        """
        return [product for product in self.products.values() if name_query in product.name]
