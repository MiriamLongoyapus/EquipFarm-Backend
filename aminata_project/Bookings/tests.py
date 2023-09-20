from django.test import TestCase
from .models import Bookings
from datetime import datetime, timedelta

class BookingsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.booking = Bookings.objects.create(
            customer_name="Mercy Cheptoo",
            equipment_name="Tractor",
            equipment_category="Farm category",
            duration=timedelta(hours=2),
            booking_date=datetime(2023, 9, 15, 10, 0, 0),
        )

    def test_customer_name_max_length(self):
        booking = Bookings.objects.get(id=self.booking.id)
        max_length = booking._meta.get_field('customer_name').max_length
        self.assertEqual(max_length, 32)

    def test_equipment_name_max_length(self):
        booking = Bookings.objects.get(id=self.booking.id)
        max_length = booking._meta.get_field('equipment_name').max_length
        self.assertEqual(max_length, 32)

    def test_equipment_category_max_length(self):
        booking = Bookings.objects.get(id=self.booking.id)
        max_length = booking._meta.get_field('equipment_category').max_length
        self.assertEqual(max_length, 32)

    def test_duration_field(self):
        booking = Bookings.objects.get(id=self.booking.id)
        self.assertIsInstance(booking.duration, timedelta)

    def test_booking_date_field(self):
        booking = Bookings.objects.get(id=self.booking.id)
        self.assertIsInstance(booking.booking_date, datetime)

