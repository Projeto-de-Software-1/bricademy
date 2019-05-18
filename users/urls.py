from django.urls import path
from .views import signup
from .views import logout_user, Login

app_name = 'users'
urlpatterns = [
    path('cadastro', signup, name="signup"),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
]
