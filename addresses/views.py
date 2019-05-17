from django.shortcuts import render, redirect
from .forms import AddressForm


def newAddress(request):
    error = False
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            error = False
            mapbox_access_token = "pk.eyJ1IjoiZG95bGVzbSIsImEiOiJjanZzZWx5bjgzNTE3M3lvajFxMmlyM3diIn0.RImU51Sa3cQqh50ZtCGBkA"

            return render(request, 'home.html', {'mapbox_access_token': mapbox_access_token})
        else:
            error = True
    else:
        form = AddressForm()
    return render(request, 'addresses/new_address.html', {'form': form, 'error': error})
