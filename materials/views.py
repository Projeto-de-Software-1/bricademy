from django.shortcuts import render, redirect, get_object_or_404
from .forms import MaterialForm
from .models import Material, Ad, Subject, Request
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def newMaterial(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Material cadastrado!')
            # messages.warning(request, 'exemplo Aviso!')
            # messages.error(request, 'exemplo Erro!')
            # messages.info(request, 'exemplo Info!')
            return redirect("materials:list_material")
        else:
            messages.warning(request, 'Erro no cadastro')
    else:
        form = MaterialForm()
        return render(request, 'materials/new_material.html',  {'form': form})


@login_required
def editMaterial(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if(material.user != request.user):
        messages.error(request, 'Este material não lhe pertence')
        return redirect('materials:list_material')
    if(material.deleted == 1):
        messages.error(request, 'Este material foi removido')
        return redirect('materials:list_material')
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            subjects = request.POST.getlist('subject')
            material = form.save(commit=False)
            material.user = request.user
            material.subject.clear()

            for subject in subjects:
                sub = Subject.objects.filter(id=subject).first()
                material.subject.add(sub)
            material.save()
            messages.success(request, 'Material atualizado com sucesso!')
            return redirect('materials:list_material')
    else:
        form = MaterialForm(instance=material)

    return render(request, 'materials/edit_material.html',
                  {'form': form, 'pk': pk, 'title': material.title, 'author': material.author})
# completar return


def excluirMaterial(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if(material.user != request.user):
        messages.error(request, 'Este material não lhe pertence')
        return redirect('materials:list_material')

    if(material.deleted == 1):
        messages.error(request, 'Este material foi removido')
        return redirect('materials:list_material')

    ad = Ad.objects.filter(material_id=pk)

    if (ad):
        messages.error(
            request, 'Material possui um Anúncio, primeiro remova-o')
        return redirect('materials:list_material')
    else:
        messages.success(request, 'Material deletado com sucesso')
        material.deleted = 1
        material.save()
        return redirect('materials:list_material')


@login_required
def ListMaterials(request):
    materials = Material.objects.filter(user=request.user, deleted=0)
    anuncios = Ad.objects.all()
    anunciados = []
    for ad in anuncios:
        for m in materials:
            if m.pk == ad.material.pk and ad.deleted == 0:
                anunciados.append(ad.material)

    return render(request, 'materials/list_material.html',  {'materials': materials, 'anunciados': anunciados})


@login_required
def minhasSolicitacoes(request):
    Solicitacoes = Request.objects.filter(user=request.user)
    materials = []
    return render(request, 'materials/minhas_solicitacoes.html',  {'solicitacoes': Solicitacoes})


@login_required
def solicitacoesRecebidas(request):
    Requests = Request.objects.all()
    Solicitacoes = []

    for req in Requests:
        # Se o dono do material for o cara que ta acessando
        # vai pegar todos as soand req.ad.deleted == 0licitacoes pros anuncios cujo o material é dele
        # mas acho que essa view seria interessante fazer algo em pegar todos os anuncios
        # e depois verificar as solicitacoes pra cada anuncios, daí da pra iterar e mostrar as solicitações
        # pros anuncios isoladas

        # resumindo seria uma pagina mostrando 'meus anuncios' e podendo clicar pra ver as solicitacoes dele
        if req.ad.material.user == request.user and req.ad.deleted == 0:
            Solicitacoes.append(req)

    return render(request, 'materials/solicitacoes_recebidas.html',  {'solicitacoes': Solicitacoes})
