from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'contador' in request.session:
        request.session['contador'] += 1
    else:
        request.session['contador'] = 1
        
    unique_id = get_random_string(length=14)
    contexto = {
        'palabra': unique_id
    }
    print(f"Palabra :", unique_id)
    return render(request, 'index.html', contexto)  

def resetear(request):
    request.session['contador'] = 0
    return redirect("/")