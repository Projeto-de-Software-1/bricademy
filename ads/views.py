from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material, Request
from django.http import HttpResponseNotFound
from .forms import AdVendaForm
from django.conf import settings
from django.contrib import messages


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
        if(ad.deleted == 0):
            material.append(ad.material)
            tipos.append(ad.ad_type)
    todos = list(zip(material, tipos))
    return render(request, 'home.html', {'materiais': todos})


def cria_anuncio(request, pk):
    # Verifica se já existe um anúncio para aquele material. Se nao tiver anuncia, senão retorna direto.
    ads = Ad.objects.filter(material=pk)
    print(ads)
    if not ads:
        print("Material NAO anunciado")
        material = get_object_or_404(Material, pk=pk)
        if(material.user != request.user):
            messages.error(request, 'Este material não lhe pertence')
            return redirect('home')
        if(material.deleted == 1):
            messages.error(request, 'Este material foi removido')
            return redirect('home')
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
                messages.success(request, 'Anúncio criado com sucesso!!')
    else:
        messages.warning(request, 'Material já anunciado')

    return redirect('home')


def venda(request,  pk):
    anuncio = get_object_or_404(Ad, material_id=pk)
    if(anuncio.deleted == 1):
        messages.error(request, 'Este anuncio foi removido pelo dono')
        return redirect('home')
    solicitacao = Request.objects.filter(ad=anuncio, user=request.user)
    if(solicitacao):
        messages.warning(
            request, 'Você ja fez uma solicitação para esse material')
        return redirect('home')
    else:
        solicitacao = Request.objects.create(ad=anuncio, user=request.user)
        messages.success(
            request, 'Solicitação enviada com sucesso')
    return redirect('home')


def emprestimo(request,  pk):
    return redirect('home')


def doacao(request,  pk):
    return redirect('home')
