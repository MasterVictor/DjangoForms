from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Usuario
# from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
# Create your views here.

class UsuarioListView(generic.ListView):
    model = Usuario
    template_name = "listUsu.html"


class UsuarioCreateView(generic.CreateView):
    model = Usuario
    fields = '__all__'
    template_name = "createUsu.html"


class UsuarioDetailView(generic.DetailView):
    model = Usuario
    template_name = "detailUsu.html"



