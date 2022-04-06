from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from goals.models import CharacterGoal

# Create your views here.

class CharacterGoalsCreateView(LoginRequiredMixin, CreateView):
    model = CharacterGoal
    template_name = "goals/create_character_goal.html"
    fields = ["name", "description", "character"]

    def get_success_url(self):
        return reverse_lazy("detail_character", args=[self.object.character_id])