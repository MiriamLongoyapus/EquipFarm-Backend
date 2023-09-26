from django.test import TestCase
from .models import HirePurchase

class HirePurchaseModelTests(TestCase):
    def test_calculate_installment_and_balance_monthly(self):
        hire_purchase = HirePurchase(
            equipment_name="Laptop",
            total_price=1000.0,
            down_payment=200.0,
            installment_period=6,
            payment_frequency='monthly'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 133.33333333333334)
        self.assertEqual(hire_purchase.remaining_balance, 800.0)

    def test_calculate_installment_and_balance_quarterly(self):
        hire_purchase = HirePurchase(
            equipment_name="Monitor",
            total_price=1500.0,
            down_payment=300.0,
            installment_period=6,
            payment_frequency='quarterly'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 66.66666666666667)
        self.assertEqual(hire_purchase.remaining_balance, 1200.0)

    def test_calculate_installment_and_balance_annually(self):
        hire_purchase = HirePurchase(
            equipment_name="Printer",
            total_price=2000.0,
            down_payment=400.0,
            installment_period=6,
            payment_frequency='annually'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 266.6666666666667)
        self.assertEqual(hire_purchase.remaining_balance, 1600.0)

    def test_calculate_installment_and_balance_invalid_frequency(self):
        hire_purchase = HirePurchase(
            equipment_name="Keyboard",
            total_price=800.0,
            down_payment=160.0,
            installment_period=4,
            payment_frequency='invalid_frequency'
        )
        installment_amount = hire_purchase.calculate_installment_and_balance()
        self.assertEqual(installment_amount, 0)
        self.assertEqual(hire_purchase.remaining_balance, 0)

    def test_save_method(self):
        hire_purchase = HirePurchase(
            equipment_name="Mouse",
            total_price=500.0,
            down_payment=100.0,
            installment_period=5,
            payment_frequency='monthly'
        )
        hire_purchase.save()
        self.assertEqual(hire_purchase.remaining_balance, 400.0)

    def test_str_representation(self):
        hire_purchase = HirePurchase(equipment_name="Laptop")
        self.assertEqual(str(hire_purchase), hire_purchase.equipment_name)
