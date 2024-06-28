from django.shortcuts import render
from django.views.generic import TemplateView
from kitchen.models import Drink
from kitchen.models import Pizza



# Create your views here.
class PizzaListTemplateView(TemplateView):
    """Отдает клиенту html-шаблон списка пицц"""
    template_name = 'pizza_list.html'


class PizzaDetailView(TemplateView):
    template_name = 'pizza_datale.html'

    def get_context_data(self, **kwargs):
        context = dict()
        pizza_obj = Pizza.objects.first()
        context['first_pizza'] = pizza_obj
        return context


class DrinkListTemplateView(TemplateView):
    """Отдает клиенту html-шаблон списка пицц"""
    template_name = 'drinks.html'

    def get_context_data(self, **kwargs):
        context = dict()
        drink = Drink.objects.first()
        context['first_drink'] = drink
        return context
