from django.urls import path

from clientes.views import home

urlpatterns = [
    path('test', home,name='home')
]
