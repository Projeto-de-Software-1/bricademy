from django.shortcuts import render
from .forms import MaterialForm
from .models import Material

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


def ListMaterials(request):
    materials = Material.objects.filter(user=request.user)
    return render(request, 'materials/list_material.html',  {'materials': materials})
