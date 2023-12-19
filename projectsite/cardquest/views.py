from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.models import PokemonCard,Trainer,Collection
from cardquest.forms import TrainerForm,PokemonCardForm,CollectionForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemon-card.html"
    paginate_by = 5
    ordering = ['name'] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PokemonCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_add.html'
    success_url = reverse_lazy('pokemon-cards')
    
class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_edit.html'
    success_url = reverse_lazy('pokemon-cards')
    
class PokemonDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemon_del.html'
    success_url = reverse_lazy('pokemon-cards')

    
    
    
    
    
    
    
    
    
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainers'
    template_name = "trainer.html"
    paginate_by = 5
    ordering = ['name'] 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')
    
    
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')










class CollectionListView(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = "collection.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection')
    
class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection')
    
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection')

    


# Create your views here.
