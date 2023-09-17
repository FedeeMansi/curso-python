from django.shortcuts import render

# Create your views here.


def inicio(req):
    return render (req,"inicio.html")

def random_pwd(req):
     return render (req,"random.html")

def guardar_credencial(req):
    return render (req,"guardar_credencial.html")

def mostrar_credencial(req):
     return render (req,"mostrar_credencial.html")






