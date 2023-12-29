from django.urls import path
from . import views

urlpatterns = [
    path('customers' , views.customers_list , name = 'customers'),
    path('customers/<int:pk>/' , views.customer_detail , name = 'single-customer'),
    path('agencies' , views.agencies_list , name = 'agencies'),
    path('agencies/<int:pk>/' , views.agency_detail , name = 'single-agency'),
    path('tours' , views.tours_list , name = 'tours'),
    path('tours/<int:pk>/' , views.tour_detail , name = 'single-tour'),

    
]