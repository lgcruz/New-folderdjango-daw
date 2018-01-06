from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index(request):
    return render(request,"mapa/index.html")
def acerca(request):
    return render(request,"mapa/acerca.html")
def contacto(request):
    return render(request,"mapa/contacto.html")
def desarrolladores(request):
    return render(request,"mapa/Desarrolladores.html")
def faq(request):
    return render(request,"mapa/faqs.html")
def galeria(request):
    return render(request,"mapa/galeria.html")
def programadores(request):
    return render(request,"mapa/programadores.html")
def timeline(request):
    return render(request,"mapa/timeline.html")

