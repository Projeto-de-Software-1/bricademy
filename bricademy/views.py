from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material
from django.http import HttpResponseNotFound
from django.conf import settings


def sobre(request):
    return render(request, 'sobre.html')


def home(request):
    anuncios = Ad.objects.all()
    material = []
    tipos = []
    for ad in anuncios:
        if(ad.deleted == 0):
            material.append(ad.material)
            tipos.append(ad.ad_type)
    todos = list(zip(material, tipos))
    return render(request, 'home.html', {'materiais': todos, 'anuncios': anuncios, 'token': settings.MAPBOX_TOKEN})
    # return render(request, 'home.html')


def homemap(request):
    anuncios = Ad.objects.filter(deleted=0)
    #material = []
    #tipos = []
    # for ad in anuncios:
    #    if(ad.deleted == 0):
    #        material.append(ad)
    # tipos.append(ad.ad_type)
    #todos = list(zip(material, tipos))
    return render(request, 'ads/list_map.html', {'anuncios': anuncios, 'token': settings.MAPBOX_TOKEN})
