from django.shortcuts import render
from django.views.generic import ListView
from .models import Trainer,PokemonCard

# Create your views here.

def home(request):
    return render(request,'home.html')


def trainer_list(request):
    return render(request,'trainer.html')

def pokemon_cards(request):
    return render(request,'pokemon-card.html')
def collections(request):
    return render(request,'collection.html')



