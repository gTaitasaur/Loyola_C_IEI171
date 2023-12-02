from django.shortcuts import render
from socios_app.models import Socios
from socios_app.forms import FormSocio
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def socios(request):
    socios = Socios.objects.all()
    data = {'socio': socios}
    return render(request, 'socios.html', data)

def agregarSocio(request):
    form = FormSocio()

    if request.method == 'POST':
        form = FormSocio(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    data = {'form': form}
    return render (request, 'agregar.html', data)

def eliminarSocio(request, id):
    socio = Socios.objects.get(pk = id)
    socio.delete()
    return redirect('socios')

def modificarSocio(request, id):
    socio = Socios.objects.get(pk = id)
    form = FormSocio(instance = socio)

    if (request.method == 'POST'):
        form = FormSocio(request.POST, instance = socio)
        if (form.is_valid()):
            form.save()
        return redirect('/socios')
  
    data = {'form': form}
    return render (request, 'agregar.html', data)