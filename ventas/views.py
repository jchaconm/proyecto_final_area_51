from django.shortcuts import render

# Create your views here.
from ventas.models import Ventas


def ultimas_ventas(request):
    ventas = Ventas.objects.filter().order_by('-id')[:5]
    return render(request, 'ultimas_ventas.html', {'ventas': ventas})