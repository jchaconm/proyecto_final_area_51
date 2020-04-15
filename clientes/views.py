from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
# Create your views here.
from clientes.forms import NuevoClienteForm

