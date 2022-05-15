from django.shortcuts import render
#aqui importamos los datos de la bd
from .models import Service
# Create your views here.

def services(request):
    #aqui estamos mostrando los objetos del back con el front
    services = Service.objects.all()
    return render(request, "services/services.html", {'services' : services})

    