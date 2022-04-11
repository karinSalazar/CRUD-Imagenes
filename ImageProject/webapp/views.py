from django.shortcuts import render, redirect
from .models import Automovil
from .forms import AutomovilForm
from django.contrib import messages
import os

def list_autos(request):
    autos = Automovil.objects.all()
    return render(request, 'bienvenido.html', {'autos': autos})



def create_autos(request):
    form = AutomovilForm(request.POST or None)

    if request.POST:
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.marca = request.POST.get('txtMarca')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = int(request.POST.get('txtAnio'))
        auto.imagen = request.FILES.get('txtImagen')
        try:
            auto.save()
            mensaje = "Guardado correctamente"
            messages.success(request, mensaje)
        except:
            mensaje = "No se ha podido guardar"
            messages.error(request, mensaje)
        return redirect('list_autos')

    return render(request, 'autos_form.html', {'form': form})





def update_autos(request, id):
    auto = Automovil.objects.get(id=id)

    if request.POST:
        if len(request.FILES) != 0:
            if len(auto.imagen) > 0:
                os.remove(auto.imagen.path)
            auto.imagen = request.FILES['imagen']
        auto.patente = request.POST.get('txtPatente')
        auto.marca = request.POST.get('txtMarca')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = int(request.POST.get('txtAnio'))
        auto.save()
        messages.success(request, "Registro actualizado con éxito")
        return redirect('/')


    return render(request, 'modificar.html', {'auto': auto})





def delete_autos(request, id):
    auto = Automovil.objects.get(id=id)

    if request.method == 'POST':
        auto.delete()
        return redirect('list_autos')

    return render(request, 'delete.html', {'auto': auto})