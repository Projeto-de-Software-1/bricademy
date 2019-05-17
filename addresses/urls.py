from django.urls import path
from .views import newAddress

app_name = 'addresses'
urlpatterns = [
    path('register', newAddress, name="new_address"),
]
