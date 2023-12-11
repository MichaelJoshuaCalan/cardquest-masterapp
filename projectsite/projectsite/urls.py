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
from cardquest.views import HomePageView, TrainerList, PokemonCardList, CollectionListView
from cardquest import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('trainers/', TrainerList.as_view(), name='trainer-list'),
    path('pokemon-cards/', PokemonCardList.as_view(), name='pokemon-cards'),
    path('collection/', CollectionListView.as_view(), name='collection'),
    # Add other paths for your views as needed
]
