from django.urls import path
from .views import BookingListView,BookingDetailView


urlpatterns = [ 
path('booking/', BookingListView.as_view(), name='booking_list_view'), 
path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking_detail_view'), 


]