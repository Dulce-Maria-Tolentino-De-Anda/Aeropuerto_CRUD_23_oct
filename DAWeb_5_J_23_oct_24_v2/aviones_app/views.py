from django.shortcuts import render
from .models import AVIONES
# Create your views here.
def listadoAviones(request):
    losaviones=AVIONES.objects.all()
    return render (request,"gestionarAviones.html", {"misaviones":losaviones})