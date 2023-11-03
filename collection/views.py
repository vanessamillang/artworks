from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import random
from collection.models import Artwork
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import Elemento

def buscar_elementos(request):
    query = request.GET.get('q', '')
    elementos = Elemento.objects.annotate(search=SearchVector('nombre', 'categorias', 'etiquetas')).filter(search=SearchQuery(query))

    # Pasa los elementos filtrados a la plantilla
    return render(request, 'collection/index.html', {'elementos': elementos, 'query': query})

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get('username')
            raw_password = f.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect('/')

    else:
        f = UserCreationForm()

    return render(request, 'registration/registration_form.html', {'form': f})


def index(request):
    count = Artwork.objects.count()
    random_artwork = None
    if count > 0:
        random_index = random.randint(0, count - 1)
        random_artwork = Artwork.objects.all()[random_index]

    return render(request, 'collection/index.html', {'artwork': random_artwork})