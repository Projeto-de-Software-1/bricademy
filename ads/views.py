from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material
from django.http import HttpResponseNotFound
from .forms import AdVendaForm
from django.conf import settings


def index(request):
    # anuncios_venda = Ad.objects.filter(ad_type=0)
    # materiais_venda = []
    # for an in anuncios_venda:
    #     materiais_venda.append(an.material)
    # return render(request, 'home.html', {'vendas': materiais_venda})
    anuncios = Ad.objects.all()
    material = []
    tipos = []
    for ad in anuncios:
        material.append(ad.material)
        tipos.append(ad.ad_type)
    todos = list(zip(material, tipos))
    return render(request, 'home.html', {'materiais' : todos})


def cria_anuncio(request, pk):
    # Verifica se já existe um anúncio para aquele material. Se nao tiver anuncia, senão retorna direto.
    ads = Ad.objects.filter(material=pk)
    print(ads)
    if not ads:
        print("Material NAO anunciado")
        material = get_object_or_404(Material, pk=pk)
        if(material.user != request.user):
            return HttpResponseNotFound("Este material não lhe pertence, voce não pode anunciar algo que não é seu, QUE PAPELÃO HEIN!")
        if(request.method == 'GET'):
            form = AdVendaForm()
            return render(request, 'ads/new.html', {'form': form, 'token': settings.MAPBOX_TOKEN})
        elif(request.method == 'POST'):
            form = AdVendaForm(request.POST)
            print(form)
            if form.is_valid():
                ad = form.save(commit=False)
                ad.material = material
                ad.ad_type = 0
                ad.save()
                error = False
    else:
        print("JA ANUNCIADO")

    return redirect('home')

def venda (request,  pk):
    return redirect('home')

def emprestimo (request,  pk):
    return redirect('home')

def doacao (request,  pk):
    return redirect('home')