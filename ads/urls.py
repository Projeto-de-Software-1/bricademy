from django.urls import path

from .views import index, new

urlpatterns = [
    path('', index, name="index"),
    path('new/<int:pk>', new, name="new"),
]
