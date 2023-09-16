

from django.urls import path
from .views import BookingsListView, BookingsDetailView

urlpatterns = [ 
    path('Bookings/', BookingsListView.as_view(), name='Bookings_list_view'), 
    path('Bookings/<int:id>/', BookingsDetailView.as_view(), name='Bookings_detail_view'), 
]




