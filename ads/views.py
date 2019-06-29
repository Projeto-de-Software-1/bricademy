from django.shortcuts import render, get_object_or_404, redirect
from materials.models import Ad, Material, Request
from django.http import HttpResponseNotFound
from .forms import AdVendaForm, AdDoacaoForm, AdEmprestimoForm
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
        print("OIOIEOSJOSDF\nsdoifjsdoif")
        material.append(ad.material)
        tipos.append(ad.ad_type)
    todos = list(zip(material, tipos))
    todos.sort(key=lambda x:x[0])
    return render(request, 'home.html', {'materiais': todos})


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
            form = AdVendaForm(request.POST)
            if not form.data['address']:
                messages.error(request, 'Selecione um endereço para o anúncio')
                return render(request, 'ads/new.html', {'form': form, 'token': settings.MAPBOX_TOKEN})
            if form.is_valid():
                ad = form.save(commit=False)
                ad.material = material
                ad.ad_type = tipo
                ad.save()
                messages.success(request, 'Anúncio criado com sucesso!!')
    else:
        messages.warning(request, 'Material já anunciado')

    return redirect('home')


#recebe o tipo de anuncio e o id do material
def vermais(request, tipo, pk):
    anuncio = get_object_or_404(Ad, material_id=pk)

    if(anuncio.deleted == 1):
        messages.error(request, 'Este anuncio foi removido pelo dono')
        return redirect('home')

    return render(request, 'ads/vermais.html', {'material': anuncio.material, 'anuncio': anuncio, 'tipo': tipo, 'token': settings.MAPBOX_TOKEN})

def venda(request,  anuncio, pk):
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
    return render(request, 'ads/venda.html', {'anuncio': anuncio, 'token': settings.MAPBOX_TOKEN})


def emprestimo(request, anuncio, pk):
    return redirect('home')


def doacao(request, anuncio, pk):
    return redirect('home')
