from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material
from django.http import HttpResponseNotFound

def home(request):
    anuncios = Ad.objects.all()
    material = []
    tipos = []
    for ad in anuncios:
        material.append(ad.material)
        tipos.append(ad.ad_type)
    todos = list(zip(material, tipos))
    return render(request, 'home.html', {'materiais' : todos})
    # return render(request, 'home.html')
