from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material
from django.http import HttpResponseNotFound

def home(request):
    anuncios_venda = Ad.objects.filter(ad_type=0)
    materiais_venda = []
    for an in anuncios_venda:
        materiais_venda.append(an.material)
    return render(request, 'home.html', {'vendas': materiais_venda})
    # return render(request, 'home.html')
