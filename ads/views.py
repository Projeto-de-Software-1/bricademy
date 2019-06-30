from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material, Request
from django.http import HttpResponseNotFound
from .forms import AdVendaForm, AdDoacaoForm, AdEmprestimoForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
        if(ad.deletado == 0):
            material.append(ad.material)
            tipos.append(ad.ad_type)
    todos = list(zip(material, tipos))
    todos.sort(key=lambda x: x[0])
    return render(request, 'home.html', {'materiais': todos})


@login_required
def cria_anuncio(request, pk, tipo):

    # Verifica se já existe um anúncio para aquele material. Se nao tiver anuncia, senão retorna direto.
    ads = Ad.objects.filter(material=pk)
    if not ads:
        material = get_object_or_404(Material, pk=pk)
        if(material.user != request.user):
            messages.error(request, 'Este material não lhe pertence')
            return redirect('home')
        if(material.deleted == 1):
            messages.error(request, 'Este material foi removido')
            return redirect('home')
        if(request.method == 'GET'):
            if(tipo == 0):
                form = AdVendaForm()
            elif(tipo == 1):
                form = AdDoacaoForm()
            else:
                form = AdEmprestimoForm()
            return render(request, 'ads/new.html', {'form': form, 'token': settings.MAPBOX_TOKEN})
       
        elif(request.method == 'POST'):

            if(tipo == 0):
                form = AdVendaForm(request.POST)
            elif(tipo == 1):
                form = AdDoacaoForm(request.POST)
            else:
                form = AdEmprestimoForm(request.POST)

            if not form.data['address']:
                messages.error(request, 'Selecione um endereço para o anúncio')
                return render(request, 'ads/new.html', {'form': form, 'token': settings.MAPBOX_TOKEN})

            if form.is_valid():
                ad = form.save(commit=False)
                ad.material = material
                ad.ad_type = tipo

                if ad.price == None:
                    ad.price = 0
                ad.save()
                messages.success(request, 'Anúncio criado com sucesso!!')
    else:
        messages.warning(request, 'Material já anunciado')

    return redirect('home')


def excluir_anuncio(request, pk):

    solicitacoes = Request.objects.all()

    for s in solicitacoes:
        if s.ad.pk == pk:
            messages.warning(request, 'Você precisa responder as solicitações sobre este anúncio')
            return redirect('materials:list_material')
    
    anuncio = get_object_or_404(Ad, material=pk)
    anuncio.deleted = 1
    anuncio.save()
    messages.success(request, 'Anúncio deletado com sucesso')
    return redirect('materials:list_material')


# recebe o tipo de anuncio e o id do material
@login_required
def vermais(request, tipo, pk):
    anuncio = get_object_or_404(Ad, material_id=pk)

    if(anuncio.deleted == 1):
        messages.error(request, 'Este anuncio foi removido pelo dono')
        return redirect('home')

    return render(request, 'ads/vermais.html', {'material': anuncio.material, 'anuncio': anuncio, 'tipo': tipo, 'token': settings.MAPBOX_TOKEN})


@login_required
def solicitacao(request,  anuncio, pk):
    anuncio = get_object_or_404(Ad, material_id=pk)
    if(anuncio.deleted == 1):
        messages.error(request, 'Este anúncio foi removido pelo dono')
        return redirect('home')

    solicitacao = Request.objects.filter(ad=anuncio, user=request.user)

    if(solicitacao):
        messages.warning(
            request, 'Você já fez uma solicitação para esse material')
        return redirect('home')
    else:
        solicitacao = Request.objects.create(ad=anuncio, user=request.user)
        messages.success(
            request, 'Solicitação enviada com sucesso')
    return render(request, 'ads/venda.html', {'anuncio': anuncio, 'token': settings.MAPBOX_TOKEN})

@login_required
def negociacao(request, pk):
    anuncio = get_object_or_404(Ad, pk=pk)
    return render(request, 'ads/venda.html', {'anuncio': anuncio, 'token': settings.MAPBOX_TOKEN})

