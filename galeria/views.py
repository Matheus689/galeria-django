from django.shortcuts import render, get_object_or_404
from .models import Pais

# Create your views here.
def home(request):
    paises = Pais.objects.all()
    return render(request, "galeria/home.html", {'paises':paises})

def pais_detail(request, id):
    pais = get_object_or_404(Pais, pk=id)
    
    context = {
        'pais': pais,
    }
    return render(request, 'galeria/pais.html', context)

def pesquisar_pais(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Pais.objects.filter(title__icontains=query)
    
    context = {
        'query': query,
        'resultados': resultados,
    }
    
    return render(request, 'galeria/pesquisa.html', context)