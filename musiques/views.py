from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Morceau, Artiste

from django.shortcuts import render

def frencky_vincent_view(request):
    return render(request, 'musiques/frencky_vincent.html')

class MorceauList(ListView):
    model = Morceau
    template_name = "musiques/morceau_list.html"
    context_object_name = "morceaux"
    paginate_by = 20

class MorceauDetailView(DetailView):
    model = Morceau
    template_name = "musiques/morceau_detail.html"
    context_object_name = "morceau"

class MorceauCreateView(CreateView):
    model = Morceau
    fields = ['titre', 'artiste', 'date_sortie']
    template_name = "musiques/morceau_form.html"
    success_url = reverse_lazy('musiques:morceau-list')

class MorceauUpdateView(UpdateView):
    model = Morceau
    fields = ['titre', 'artiste', 'date_sortie']
    template_name = "musiques/morceau_form.html"
    success_url = reverse_lazy('musiques:morceau-list')

class MorceauDeleteView(DeleteView):
    model = Morceau
    template_name = "musiques/morceau_confirm_delete.html"
    success_url = reverse_lazy('musiques:morceau-list')

class ArtisteListView(ListView):
    model = Artiste
    template_name = "musiques/artiste_list.html"
    context_object_name = "artistes"

class ArtisteCreateView(CreateView):
    model = Artiste
    fields = ['nom']
    template_name = "musiques/artiste_form.html"
    success_url = reverse_lazy('musiques:artiste-list')

class ArtisteUpdateView(UpdateView):
    model = Artiste
    fields = ['nom']
    template_name = "musiques/artiste_form.html"
    success_url = reverse_lazy('musiques:artiste-list')