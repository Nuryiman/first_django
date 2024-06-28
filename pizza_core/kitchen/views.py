from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class PizzaListTemplateView(TemplateView):
    """Отдает клиенту html-шаблон списка пицц"""
    template_name = 'pizza_list.html'

