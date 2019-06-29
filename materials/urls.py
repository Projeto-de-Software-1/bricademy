from django.urls import path
from .views import newMaterial, minhasSolicitacoes, solicitacoesRecebidas, ListMaterials, editMaterial, excluirMaterial

app_name = 'materials'
urlpatterns = [
    path('new', newMaterial, name="new_material"),
    path('list', ListMaterials, name="list_material"),
    path('solicitacoes', minhasSolicitacoes, name="minhas_solicitacoes"),
    path('recebidas', solicitacoesRecebidas, name="solicitacoes_recebidas"),
    path('edit/<int:pk>', editMaterial, name="edit_material"),
    path('excluir/<int:pk>', excluirMaterial, name="excluir_material")
]
