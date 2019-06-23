from django.shortcuts import render, redirect, get_object_or_404
from .forms import MaterialForm
from .models import Material, Ad, Subject
from django.contrib import messages

# Create your views here.


def newMaterial(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Material cadastrado!')
            messages.warning(request, 'exemplo Aviso!')
            messages.error(request, 'exemplo Erro!')
            messages.info(request, 'exemplo Info!')
            return redirect("materials:list_material")
        else:
            messages.warning(request, 'Erro no cadastro')
    else:
        form = MaterialForm()
        return render(request, 'materials/new_material.html',  {'form': form})


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


def ListMaterials(request):
    materials = Material.objects.filter(user=request.user, deleted=0)

    return render(request, 'materials/list_material.html',  {'materials': materials})


def ad_teste(request):
    ad = Ad.objects.first()
    print(ad.material.user.id)
