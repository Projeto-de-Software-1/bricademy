from django.urls import path
from .views import index, venda, vermais, doacao, emprestimo, cria_anuncio

app_name = 'ads'
urlpatterns = [
    path('', index, name="index_url"),
    path('new/<int:pk>/<int:tipo>', cria_anuncio, name="ad_url"),
    path('vermais/<int:tipo>/<int:pk>', vermais, name="vermais_url"),
    path('venda/<int:anuncio>/<int:pk>', venda, name="venda_url"),
    path('doacao/<int:anuncio>/<int:pk>', doacao, name="doacao_url"),
    path('emprestimo/<int:anuncio>/<int:pk>', emprestimo, name="emprestimo_url"),
]
