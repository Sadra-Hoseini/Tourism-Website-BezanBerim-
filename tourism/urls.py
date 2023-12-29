from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.home , name = 'home'),
    path('book/' , views.book , name = 'book'),
    path('tours/' , views.tours , name = 'tours'),
    path('tour_item/<int:pk>/' , views.display_tour_items , name = 'tour_item'),
    path('services/' , views.services , name = 'services'),
    path('gallery/' , views.gallery , name = 'gallery'),
    path('review/' , views.review , name = 'review'),
    path('contact/' , views.contact , name = 'contact'),
    path('register/' , views.register , name = 'register'),
    path('accounts/forgot_password/' , views.forgot_password , name = 'forgot_password'),
    path('accounts/forgot_password/reset_password/<username>/<id>' , views.reset_password , name = 'reset_password'),
    



]