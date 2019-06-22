from django.urls import path
from .views import newMaterial, ListMaterials, editMaterial,ad_teste

app_name = 'materials'
urlpatterns = [
    path('new', newMaterial, name="new_material"),
    path('list', ListMaterials, name="list_material"),
    path('edit/<int:pk>', editMaterial, name="edit_material"),
    path('teste', ad_teste)
]