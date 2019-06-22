from .forms import AddressForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm, AddressForm
from .models import Address


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

def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            update_session_auth_hash(request, profile_form.user)
            return render(request, 'users/profile.html', {})
        else:
            error = True
    else:
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'profile_form': profile_form})

class Login(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = 'registration/login.html'
    redirect_authenticated_user = 'home'


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    address = Address.objects.filter(user=request.user).first()
    return render(request, 'users/profile.html',  {'address': address})


def newAddress(request):
    error = False
    mapbox_access_token = ""

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            error = False

            return render(request, 'home.html', {'mapbox_access_token': mapbox_access_token})
        else:
            error = True
    else:
        form = AddressForm()
    return render(request, 'users/new_address.html',  {'form': form, 'mapbox_access_token': mapbox_access_token,  'error': error})
