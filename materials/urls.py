from django.urls import path
from .views import newMaterial, ListMaterials

app_name = 'materials'
urlpatterns = [
    path('new', newMaterial, name="new_material"),
    path('list', ListMaterials, name="list_material"),

]
