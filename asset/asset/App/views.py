from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["goods"] = Goods.objects.all()
            return context
        