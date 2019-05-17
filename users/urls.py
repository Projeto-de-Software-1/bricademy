from django.urls import path
from .views import signup

app_name = 'users'
urlpatterns = [
    path('cadastro', signup, name="signup"),
]
