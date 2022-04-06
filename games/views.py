from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from games.models import Game, Character

# Create your views here.


class GameListView(LoginRequiredMixin, ListView):
    model = Game
    template_name = "games/list_games.html"

    def get_queryset(self):
        return Game.objects.filter(members=self.request.user)


class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = "games/detail_game.html"
    context_object_name = "game_detail"

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    template_name = "games/create_game.html"
    fields = ["name", "description", "members"]
    success_url = reverse_lazy('home')
    

class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = "characters/detail_character.html"
    context_object_name = "character_detail"

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    template_name = "characters/create_character.html"
    fields = ["name", "summary", "playersclass", "goals", "game"]


    def form_valid(self, form):
        character = form.save(commit=False)
        character.user = self.request.user
        character.save()
        return redirect("home")

class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    model = Character
    template_name = "characters/update_character.html"
    context_object_name = "character_update"
    fields = ["name", "summary", "playersclass", "goals", "game"]
    success_url = reverse_lazy("character_detail")
