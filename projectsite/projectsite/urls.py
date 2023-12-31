"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cardquest.views import (
    HomePageView, 
    TrainerList,TrainerCreateView, TrainerUpdateView, TrainerDeleteView,  
    PokemonCardList,PokemonCreateView,PokemonUpdateView,PokemonDeleteView,
    CollectionListView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    
    path('trainers/', TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add/', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>/', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainers/delete/<int:pk>/', TrainerDeleteView.as_view(), name='trainer-delete'),
    
    
    path('pokemon-cards/', PokemonCardList.as_view(), name='pokemon-cards'),
    path('pokemoncard_list/add', PokemonCreateView.as_view(), name='pokemon_add'),
    path('pokemon-edit/<int:pk>/', PokemonUpdateView.as_view(), name='pokemon_edit'),
    path('pokemon-delete/<int:pk>/', PokemonDeleteView.as_view(), name='pokemon_delete'),
    
    
    
    

    
    path('collection/', CollectionListView.as_view(), name='collection'),
    path('collection_list/add/', CollectionCreateView.as_view(), name='collection_add'),
    path('collection-edit/<int:pk>/', CollectionUpdateView.as_view(), name='collection_edit'),
    path('collection-delete/<int:pk>/', CollectionDeleteView.as_view(), name='collection_delete'),
    
    
    
    
]

# Static files serving configuration
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)