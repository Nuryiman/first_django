from django.contrib import admin
from .models import Pizza, Drink, Sushi, Burger


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image']


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'volume', 'is_alcohol', 'consist', 'price']


@admin.register(Sushi)
class SushiAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'image']


@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
