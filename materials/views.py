from django.shortcuts import render, redirect, get_object_or_404
from .forms import MaterialForm
from .models import Material, Ad

# Create your views here.


def newMaterial(request):
    error = False
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            error = False
            # TODO
            # ver se esse é o melhor jeito
            materials = Material.objects.filter(user=request.user)
            return render(request, 'materials/list_material.html',  {'materials': materials})
        else:
            error = True
    else:
        form = MaterialForm()
        return render(request, 'materials/new_material.html',  {'form': form,  'error': error})


def editMaterial(request, pk):
    material = get_object_or_404(Material, pk=pk)
    print("OIOI")
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save(commit=False)
            material.user = request.user
            material.save()
            return redirect('materials:list_material')
    else:
        form = MaterialForm(instance=material)

    return render(request, 'materials/edit_material.html',
                  {'form': form, 'pk': pk, 'title': material.title, 'author': material.author})
#completar return



def ListMaterials(request):
    materials = Material.objects.filter(user=request.user)
    return render(request, 'materials/list_material.html',  { 'materials': materials })


def ad_teste(request):
    ad = Ad.objects.first()
    print(ad.material.user.id)