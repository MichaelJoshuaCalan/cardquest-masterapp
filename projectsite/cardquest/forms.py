from django.forms import ModelForm
from django import forms
from .models import Trainer, Collection, PokemonCard

class TrainerForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Trainer
        fields = "__all__"
        
class PokemonCardForm(forms.ModelForm):
    
    class Meta:
        model = PokemonCard
        fields = '__all__'


class CollectionForm(forms.ModelForm):
    
    class Meta:
        model = Collection
        fields = '__all__'