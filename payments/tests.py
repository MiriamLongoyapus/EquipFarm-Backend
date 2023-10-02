from django.test import TestCase
from .models import Payment

class PaymentModelTests(TestCase):
    def test_payment_str_representation(self):
        equipment_name = "Laptop"
        price = 500.0
        payment = Payment.objects.create(equipment_name=equipment_name, price=price)
        expected_str = f"Payment for {equipment_name} on {payment.date}"
        self.assertEqual(str(payment), expected_str)

    def test_payment_creation(self):
        equipment_name = "Monitor"
        price = 300.0
        payment = Payment.objects.create(equipment_name=equipment_name, price=price)
        self.assertEqual(payment.equipment_name, equipment_name)
        self.assertEqual(payment.price, price)

    def test_payment_default_date(self):
        equipment_name = "Keyboard"
        price = 50.0
        payment = Payment.objects.create(equipment_name=equipment_name, price=price)
        self.assertIsNotNone(payment.date)
