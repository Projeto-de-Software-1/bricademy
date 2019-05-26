from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import signup
from .views import logout_user, Login, profile, newAddress

app_name = 'users'
urlpatterns = [
    path('perfil', profile, name="perfil"),
    path('cadastro', signup, name="signup"),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                                                 email_template_name='registration/password_reset_email.html',
                                                                 subject_template_name='registration/password_reset_subject.txt',
                                                                 success_url=reverse_lazy(
                                                                     'users:password_reset_done')
                                                                 ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',
                                                                                                 success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('endereco', newAddress, name='new_address'),
]
