from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Payment

class PaymentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.payment = Payment.objects.create(
            payment_amount=100.00,
            payment_date=timezone.now(),
            user=self.user,
            validity_period=timezone.timedelta(hours=1)  # Corrected value
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.payment_amount, 100.00)
        self.assertAlmostEqual(self.payment.payment_date, timezone.now(), delta=timezone.timedelta(minutes=1))
        self.assertEqual(self.payment.user, self.user)
        self.assertEqual(self.payment.validity_period, timezone.timedelta(hours=1))  # Corrected value

    def test_payment_str(self):
        expected_str = f"{self.user.username}'s Payment"
        self.assertEqual(str(self.payment), expected_str)

    def test_payment_amount_max_digits(self):
        max_digits = Payment._meta.get_field('payment_amount').max_digits
        self.assertEqual(max_digits, 10)

    def test_payment_amount_decimal_places(self):
        decimal_places = Payment._meta.get_field('payment_amount').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_user_payment_relationship(self):
        payments = self.user.payment_payments.all()
        self.assertEqual(payments.count(), 1)
        self.assertEqual(payments.first(), self.payment)

    def test_validity_period_type(self):
        validity_period_type = Payment._meta.get_field('validity_period').get_internal_type()
        self.assertEqual(validity_period_type, 'DurationField')

