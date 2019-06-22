from django.urls import path
from .views import index, venda, doacao, emprestimo, cria_anuncio

app_name = 'ads'
urlpatterns = [
    path('', index, name="index_url"),
    path('new/<int:pk>', cria_anuncio, name="ad_url"),
    path('venda/<int:pk>', venda, name="venda_url"),
    path('doacao/<int:pk>', doacao, name="doacao_url"),
    path('emprestimo/<int:pk>', emprestimo, name="emprestimo_url"),
]
