from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .forms import ProfileForm


# Create your views here.
def signup(request):
    error = False
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            error = False
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth = form.cleaned_data.get(
                'birth')
            user.profile.CPF = form.cleaned_data.get('CPF')
            user.save()
            return render(request, 'registration/confirmation.html', {})
        else:
            error = True
    else:
        form = ProfileForm()
    return render(request, 'registration/signup.html', {'form': form, 'error': error})


class Login(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = 'registration/login.html'
    redirect_authenticated_user = 'home'


def logout_user(request):
    logout(request)
    return redirect('home')
