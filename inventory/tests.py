# inventory/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from products.models import Product
from warehouses.models import Warehouse
from inventory.models import Inventory, StockMovement
from inventory.services.stock import process_stock_movement

User = get_user_model()

class StockMovementServiceTests(TestCase):
    
    def setUp(self):
        """
        This runs before every test. We use it to set up dummy data.
        """
        self.user = User.objects.create_user(username="testadmin", password="password")
        
        self.warehouse = Warehouse.objects.create(
            name="Main Warehouse", 
            code="WH-01"
        )
        
        self.product = Product.objects.create(
            sku="LAPTOP-01", 
            name="MacBook Pro", 
            unit="pcs"
        )
        
        self.inventory = Inventory.objects.create(
            warehouse=self.warehouse,
            product=self.product,
            quantity=10, # Starting with 10 laptops in stock
            minimum_quantity=5
        )

    def test_successful_purchase_movement(self):
        """
        Test that a PURCHASE movement correctly adds to the inventory quantity.
        """
        movement = process_stock_movement(
            inventory=self.inventory,
            movement_type=StockMovement.MovementType.PURCHASE,
            quantity=5,
            performed_by=self.user,
        )
        
        # Refresh the inventory from the database to get the updated quantity
        self.inventory.refresh_from_db()
        
        # 10 (initial) + 5 (purchased) should equal 15
        self.assertEqual(self.inventory.quantity, 15)
        self.assertEqual(movement.movement_type, StockMovement.MovementType.PURCHASE)

    def test_successful_sale_movement(self):
        """
        Test that a SALE movement correctly deducts from the inventory quantity.
        """
        process_stock_movement(
            inventory=self.inventory,
            movement_type=StockMovement.MovementType.SALE,
            quantity=3,
            performed_by=self.user,
        )
        
        self.inventory.refresh_from_db()
        
        # 10 (initial) - 3 (sold) should equal 7
        self.assertEqual(self.inventory.quantity, 7)

    def test_insufficient_stock_raises_error(self):
        """
        Test that trying to sell more than we have raises a ValidationError.
        """
        # We only have 10. Trying to sell 15 should trigger an error!
        with self.assertRaises(ValidationError) as context:
            process_stock_movement(
                inventory=self.inventory,
                movement_type=StockMovement.MovementType.SALE,
                quantity=15,
                performed_by=self.user,
            )
        
        self.assertIn("Not enough stock", str(context.exception))