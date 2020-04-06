from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.


def home(request):
    return HttpResponse('Hello, World!')

def beautifulSoup(request):
    return HttpResponse('Hello, World!')

def test(novel):

    search_obj = novel.replace(' ','_')

    URL = f'https://es.wikipedia.org/wiki/{search_obj}'
    print(URL)
    page = requests.get(URL)
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    seccion_argumento = soup.find(id='Argumento')
    if not (contenido_argumento := seccion_argumento.findNext('p').text):
        contenido_argumento = seccion_argumento.parent().findNext('p').text
    return contenido_argumento