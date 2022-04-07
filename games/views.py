from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from games.models import Game, Character

# Create your views here.

# === Game Views ===
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

    def form_valid(self, form):
        game = form.save(commit=False)
        game.user = self.request.user
        game.save()
        form.save_m2m()
        return redirect("show_game", pk=game.id)


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = "games/delete_game.html"
    success_url = reverse_lazy("home")
    context_object_name = "game_delete"

class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = "games/update_game.html"
    context_object_name = "game_update"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse_lazy("show_game", args=[self.object.id])
    
# === Character Views ===
class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = "characters/detail_character.html"
    context_object_name = "character_detail"

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    template_name = "characters/create_character.html"
    fields = ["name", "summary", "playersclass"]


    def form_valid(self, form):
        character = form.save(commit=False)
        game_id = self.kwargs["game_id"]
        game = Game.objects.get(id=game_id)
        character.user = self.request.user
        character.game = game
        character.save()
        form.save_m2m()
        return redirect("detail_character", pk=character.id)


class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    model = Character
    template_name = "characters/update_character.html"
    context_object_name = "character_update"
    fields = ["name", "summary", "playersclass"]

    def get_success_url(self):
        return reverse_lazy("detail_character", args=[self.object.id])
