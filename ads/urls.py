from django.urls import path
from .views import index, solicitacao, vermais, negociacao, excluir_anuncio, cria_anuncio, meusanuncios, solicitacoesanuncio, aceitar
app_name = 'ads'
urlpatterns = [
    path('', index, name="index_url"),
    path('novo/<int:pk>/<int:tipo>', cria_anuncio, name="ad_url"),
    path('excluir/<int:pk>', excluir_anuncio, name="excluir_url"),
    path('vermais/<int:tipo>/<int:pk>', vermais, name="vermais_url"),
    path('solicitacao/<int:anuncio>/<int:pk>',
         solicitacao, name="solicitacao_url"),
    path('negociacao/<int:pk>', negociacao, name="negociacao_url"),
    path('anuncios/', meusanuncios, name="meus_anuncios"),
    path('solicitacoes/<int:pk>', solicitacoesanuncio,
         name='solicitacoes_anuncio'),
    path('aceitar/<int:ad_pk>/<int:req_pk>', aceitar, name="aceitar"),
]
