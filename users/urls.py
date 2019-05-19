from django.urls import path
from .views import signup
from .views import logout_user, Login, profile, newAddress

app_name = 'users'
urlpatterns = [
    path('perfil', profile, name="perfil"),
    path('cadastro', signup, name="signup"),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('endereco', newAddress, name='new_address')
]
