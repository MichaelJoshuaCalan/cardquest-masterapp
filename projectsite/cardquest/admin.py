from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email","created_at","updated_at",)
    search_fields = ("name",)

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "card_type", "hp", "attack","created_at","updated_at",)
    search_fields = ("name", "rarity", "card_type")

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("trainer", "card", "collection_date","created_at","updated_at",)
    search_fields = ("trainer__name", "card__name", "collection_date")
