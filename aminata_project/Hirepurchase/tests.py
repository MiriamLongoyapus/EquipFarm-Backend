from django.test import TestCase
from .models import HirePurchase

class HirePurchaseModelTests(TestCase):
    # ... Existing test cases ...

    def test_calculate_installment_and_balance_semi_annually(self):
        hire_purchase = HirePurchase(
            equipment_name="Tablet",
            total_price=1200.0,
            down_payment=240.0,
            installment_period=6,
            payment_frequency='semi_annually'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 120.0)
        self.assertEqual(hire_purchase.remaining_balance, 960.0)

    def test_calculate_installment_and_balance_invalid_period(self):
        hire_purchase = HirePurchase(
            equipment_name="Scanner",
            total_price=1000.0,
            down_payment=200.0,
            installment_period=-3,  # Invalid negative period
            payment_frequency='monthly'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 0)
        self.assertEqual(hire_purchase.remaining_balance, 0)

    def test_calculate_installment_and_balance_zero_down_payment(self):
        hire_purchase = HirePurchase(
            equipment_name="Printer",
            total_price=800.0,
            down_payment=0.0,
            installment_period=4,
            payment_frequency='monthly'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 200.0)
        self.assertEqual(hire_purchase.remaining_balance, 800.0)


    def test_str_representation(self):
        hire_purchase = HirePurchase(equipment_name="Laptop")
        self.assertEqual(str(hire_purchase), hire_purchase.equipment_name)


