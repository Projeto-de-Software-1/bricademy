from .forms import AddressForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm, AddressForm
from .models import Address
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth = form.cleaned_data.get(
                'birth')
            user.profile.CPF = form.cleaned_data.get('CPF')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.save()

            return redirect('users:login')
        else:
            # error
            pass
    else:
        form = ProfileForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            profile_form.save()
            #update_session_auth_hash(request, profile_form.user)
            user = authenticate(request, username=username,
                                password=password)

            if user is not None:
                user.profile.birth = profile_form.cleaned_data.get(
                    'birth')
                user.profile.CPF = profile_form.cleaned_data.get('CPF')
                user.profile.avatar = profile_form.cleaned_data.get('avatar')
                user.save()
                login(request, user)
                messages.success(request, 'Dados atualizados com sucesso!!')
            else:
                messages.error(request, 'Falha ao atualizar os dados')

            return render(request, 'users/profile.html', {})
        else:
            messages.error(request, 'Falha ao atualizar os dados')
    else:
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'profile_form': profile_form})


class Login(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = 'registration/login.html'
    redirect_authenticated_user = 'home'


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    address = Address.objects.filter(user=request.user).first()
    return render(request, 'users/profile.html',  {'address': address})


@login_required
def newAddress(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            old_address = Address.objects.filter(user=request.user)
            if(old_address):
                old_address.delete()
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Endereço salvo com sucesso!')

            return redirect('users:perfil')
        else:
            messages.error(request, 'Falha ao salvar endereço')
            return redirect('users:perfil')
    else:
        try:
            old_address = Address.objects.get(user=request.user)
            form = AddressForm(instance=old_address)
        except:
            form = AddressForm()
        return render(request, 'users/new_address.html', {'form': form})
