from django.test import TestCase
from django.contrib.auth.models import User  
from django.utils import timezone
from .models import Payment
from django.core.exceptions import ValidationError

class PaymentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )


    def test_payment_clean_method(self):
        payment = Payment(
            payment_amount=100.00,
            payment_date_time=timezone.now(),
            user=self.user,
            validity_period='01:00:00'
        )
        payment.clean()  

    def test_payment_clean_method_invalid_payment_date(self):
        with self.assertRaises(ValidationError):
            payment = Payment(
                payment_amount=100.00,
                payment_date_time=timezone.now() + timezone.timedelta(days=1),
                user=self.user,
                validity_period='01:00:00'
            )
            payment.clean()

    def test_payment_creation(self):
        payment = Payment.objects.create(
            payment_amount=100.00,
            payment_date_time=timezone.now(),
            user=self.user,
            validity_period='01:00:00'
        )

        self.assertEqual(payment.payment_amount, 100.00)
        self.assertEqual(payment.user, self.user)
        self.assertIsNotNone(payment.payment_date_time)
        self.assertIsNotNone(payment.validity_period)

    def test_payment_string_representation(self):
        payment = Payment.objects.create(
            payment_amount=50.00,
            payment_date_time=timezone.now(),
            user=self.user,
            validity_period='02:00:00'
        )

        expected_string = f"Payment of {payment.payment_amount}"
        self.assertEqual(str(payment), expected_string)

    def test_payment_validity_period_positive(self):
        payment = Payment(
            payment_amount=100.00,
            payment_date_time=timezone.now(),
            user=self.user,
            validity_period='12:30:00' 
        )
        payment.clean() 

    def test_payment_amount_greater_than_zero(self):
        
        payment = Payment(
            payment_amount=50.00,
            payment_date_time=timezone.now(),
            user=self.user,
            validity_period='01:00:00'
        )
        payment.clean()  
    def test_payment_amount_less_than_zero(self):
        with self.assertRaises(ValidationError):
            payment = Payment(
                payment_amount=-50.00,
                payment_date_time=timezone.now(),
                user=self.user,
                validity_period='01:00:00'
            )
            payment.clean()

    def test_payment_validity_period_invalid_format(self):
        with self.assertRaises(ValidationError):
            payment = Payment(
                payment_amount=80.00,
                payment_date_time=timezone.now(),
                user=self.user,
                validity_period='invalid_format'
            )
            payment.clean()


  
