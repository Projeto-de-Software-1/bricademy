from django.urls import path

from .views import index, venda

app_name = 'ads'
urlpatterns = [
    path('', index, name="index"),
    path('new/<int:pk>', venda, name="venda"),
]
