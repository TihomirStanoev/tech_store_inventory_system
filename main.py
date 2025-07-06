from inventory import Inventory
from products.laptop import Laptop
from products.smartphone import Smartphone
from products.gaming_console import GamingConsole

def main_simulation():
    """
    A main simulation to demonstrate the inventory system functionality.
    """
    print("--- START SIMULATION ---")
    
    # 1. Create inventory for our store
    tech_store_inventory = Inventory("Future Tech Store")
    print(f"\nInventory created for store: '{tech_store_inventory.name}'")
    
    # --- 2. Create different products ---
    print("\n--- Create different products ---")
    try:
        # Create laptop
        laptop = Laptop(
            name="Ultrabook Pro X1", 
            price=2800, 
            battery_capacity_mah=5000, 
            processor="Intel Core i7-12700H", 
            ram=16
        )
        
        # Create smartphone
        smartphone = Smartphone(
            name="Galaxy Supernova", 
            price=1950, 
            bluetooth_version="5.3", 
            wifi_standard="802.11ax", 
            battery_capacity_mah=4800, 
            screen_size=6.7, 
            camera_megapixels=108
        )
        
        # Create gaming console
        console = GamingConsole(
            name="PlayStation 6", 
            price=1100, 
            controller_type="DualSense Edge", 
            storage_gb=1024
        )
        
        # Create a second laptop for tests
        laptop_2 = Laptop(
            name="WorkBook Basic",
            price=1300,
            battery_capacity_mah=3500,
            processor="AMD Ryzen 5",
            ram=8
        )

        print("Products created successfully.")
   
    except ValueError as e:
        print(f"Error while creating a product: {e}")
        return # Stop simulation if there is a problem

    # --- 3. Add products to inventory ---
    print("\n--- Add products to inventory ---")
    tech_store_inventory.add_product(laptop)
    tech_store_inventory.add_product(smartphone)
    tech_store_inventory.add_product(console)
    tech_store_inventory.add_product(laptop_2)
    
    # Try to add an existing product (expect fail):
    print("\nTrying to add an existing product (expecting failure):")
    if not tech_store_inventory.add_product(laptop):
        print(f"Product with ID {laptop.product_id} already exists. Not added again.")

    # --- 4. FULL INVENTORY REPORT (polymorphism demo) ---
    print("\n\n--- FULL INVENTORY REPORT ---")
    print(tech_store_inventory.generate_stock_report())
    
    # --- 5. TEST PRODUCT METHODS ---
    print("\n\n--- TEST PRODUCT METHODS ---")
    
    # Apply a discount
    print(f"\nCurrent price for {laptop.name}: {laptop.price:.2f}$")
    laptop.apply_discount(10)
    print(f"Price for {laptop.name} after 10% discount: {laptop.price:.2f}$")
    
    # 'Buying' the products to start their warranty
    laptop.buy()
    smartphone.buy()
    console.buy()
    print("\nThe laptop, smartphone, and console are 'purchased'. Their warranties start now.")
    
    # Check warranty
    print(f"Warranty for {laptop.name} is active? -> {laptop.is_warranty_active()}")
    
    # Use device with a battery
    print(f"\nCurrent charge for {smartphone.name}: {smartphone.current_charge_percentage}%")
    smartphone.use_device(hours=5, power=200) # power is in mA
    print(f"Charge for {smartphone.name} after 5 hours of use: {smartphone.current_charge_percentage}%")
    
    # --- 6. TEST INVENTORY METHODS ---
    print("\n\n--- TEST INVENTORY METHODS ---")
    
    # Search by ID
    found_product = tech_store_inventory.find_product(console.product_id)
    if found_product:
        print(f"\nFound product by ID ({console.product_id}): {found_product.name}")
        
    # Search by name
    laptops_found = tech_store_inventory.get_products_by_name("Book")
    print(f"\nFound products with 'Book' in name ({len(laptops_found)} count):")
    for item in laptops_found:
        print(f"- {item.name}")
        
    # Charging all devices with batteries...
    print("\nCharging all devices with batteries...")
    tech_store_inventory.charge_all_devices()
    print(f"Current charge for {smartphone.name}: {smartphone.current_charge_percentage}%")
    print(f"Current charge for {laptop.name}: {laptop.current_charge_percentage}%")
    
    # --- 7. Remove a product ---
    print("\n--- Remove a product ---")
    product_to_remove_id = laptop_2.product_id
    if tech_store_inventory.remove_product(product_to_remove_id):
        print(f"Product with ID {product_to_remove_id} ({laptop_2.name}) removed successfully.")
    
    print("\n--- INVENTORY REPORT AFTER REMOVAL ---")
    print(tech_store_inventory.generate_stock_report())
    
    print("\n--- SIMULATION ENDED ---")


# This is standard practice in Python, it allows the file to be imported
# into other files without running the code automatically.
if __name__ == "__main__":
    main_simulation()
