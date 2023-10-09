from django.test import TestCase
from .models import Rentals

class RentalsModelTests(TestCase):
    def test_calculate_total_cost_week(self):
        rental = Rentals(
            equipment_name="Laptop",
            rental_price=100.0,
            rental_period=2,
            duration_period='week'
        )
        rental.calculate_total_cost()
        self.assertEqual(rental.total_rental_cost, 200.0)

    def test_calculate_total_cost_day(self):
        rental = Rentals(
            equipment_name="Monitor",
            rental_price=50.0,
            rental_period=5,
            duration_period='day'
        )
        rental.calculate_total_cost()
        self.assertEqual(rental.total_rental_cost, 250.0)

    def test_calculate_total_cost_invalid_duration(self):
        rental = Rentals(
            equipment_name="Keyboard",
            rental_price=20.0,
            rental_period=3,
            duration_period='invalid_duration'
        )
        rental.calculate_total_cost()
        self.assertEqual(rental.total_rental_cost, 0)

    def test_save_method(self):
        rental = Rentals(
            equipment_name="Printer",
            rental_price=30.0,
            rental_period=4,
            duration_period='week'
        )
        rental.save()
        self.assertEqual(rental.total_rental_cost, 120.0)

    def test_str_representation(self):
        rental = Rentals(equipment_name="Laptop")
        expected_str = f"Rental for {rental.equipment_name}"
        self.assertEqual(str(rental), expected_str)
    
    
    # def test_str_representation(self):
    #     rental = Rentals(equipment_name="Laptop")
    #     expected_str = f"Rental for {rental.equipment_name}"
    #     self.assertEqual(str(rental), expected_str)
  