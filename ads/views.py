from django.shortcuts import render, get_object_or_404
from materials.models import Ad, Material
from django.http import HttpResponseNotFound
from .forms import AdVendaForm


def index(request):
    anuncios_venda = Ad.objects.filter(ad_type=0)
    materiais_venda = []
    for an in anuncios_venda:
        materiais_venda.append(an.material)
    return render(request, 'ads/index.html', {'vendas': materiais_venda})


def new(request, pk=0):
    material = get_object_or_404(Material, pk=pk)
    if(material.user != request.user):
        return HttpResponseNotFound("Este material não lhe pertence, voce não pode anunciar algo que não é seu, QUE PAPELÃO HEIN!")
    if(request.method == 'GET'):
        form = AdVendaForm()
        return render(request, 'ads/new.html', {'form': form})
    elif(request.method == 'POST'):
        form = AdVendaForm(request.POST)
        # form. = 0  # venda
        if form.is_valid():
            ad = form.save(commit=False)
            ad.material = material
            ad.ad_type = 0
            ad.save()
            error = False
    return render(request, 'ads/index.html')
