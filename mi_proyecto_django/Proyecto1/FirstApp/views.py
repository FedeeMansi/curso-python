from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpRequest
from .forms import ContactForm
from .models import Message
from django.http import JsonResponse
# Create your views here.


def inicio(req):
    return render (req,"inicio.html")

def random_pwd(req):
     return render (req,"random.html")

def guardar_credencial(req):
    return render (req,"guardar_credencial.html")

def authentication (req):
     return render (req,"authentication.html")

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Crea una nueva instancia del modelo Message y guárdala en la base de datos
            message_instance = Message(name=name, email=email, phone=phone, message=message)
            message_instance.save()

            # Devuelve una respuesta JSON para indicar que el mensaje se ha guardado
            return JsonResponse({'message': 'Mensaje guardado correctamente'})

    # En caso de que no sea una solicitud POST válida o el formulario no sea válido
    return JsonResponse({'error': 'Error al procesar el formulario'}, status=400)
    



