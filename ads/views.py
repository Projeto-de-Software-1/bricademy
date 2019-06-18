from django.shortcuts import render
from materials.models import Ad


def index(request):
    anuncios_venda = Ad.objects.filter(ad_type=0)
    materiais_venda = []
    for an in anuncios_venda:
        materiais_venda.append(an.material)
    return render(request, 'ads/index.html', {'vendas': materiais_venda})
