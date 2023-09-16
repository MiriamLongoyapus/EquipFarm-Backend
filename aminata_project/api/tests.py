from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Payment
from datetime import datetime, timedelta

class PaymentAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test payment
        self.payment = Payment.objects.create(
            payment_amount=100.00,
            payment_date_time=datetime.now(),
            user=self.user,
            validity_period=timedelta(days=30)
        )

        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_create_payment(self):
        url = reverse('payment-list')  # Replace with your API endpoint URL
        data = {
            'payment_amount': 200.00,
            'payment_date_time': datetime.now(),
            'validity_period': timedelta(days=30).total_seconds(),
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_payment_list(self):
        url = reverse('payment-list')  # Replace with your API endpoint URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming you have only one payment in the database

    def test_get_payment_detail(self):
        url = reverse('payment-detail', kwargs={'pk': self.payment.id})  # Replace with your API endpoint URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payment_amount'], '100.00')  # Assuming you want to test a specific field

    def test_update_payment(self):
        url = reverse('payment-detail', kwargs={'pk': self.payment.id})  # Replace with your API endpoint URL
        data = {
            'payment_amount': 150.00,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(self.payment.payment_amount, 150.00)

    def test_delete_payment(self):
urlpatterns = [
        path('payment/', PaymentListView.as_view(), name='payment_list_view'),
        path('payment/<int:id>/', PaymentDetailView.as_view(), name='payment_detail_view'),
]        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Payment.objects.filter(pk=self.payment.id).exists())
