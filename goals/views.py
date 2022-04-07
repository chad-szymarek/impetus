from django.shortcuts import redirect
from django.urls import LocalePrefixPattern, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from goals.models import CharacterGoal
from games.models import Character

# Create your views here.

class CharacterGoalsCreateView(LoginRequiredMixin, CreateView):
    model = CharacterGoal
    template_name = "goals/create_character_goal.html"
    fields = ["name", "description"]

    def form_valid(self, form):
        character_goal = form.save(commit=False)
        goal_id = self.kwargs["goal_id"]
        goal = Character.objects.get(id=goal_id)
        character_goal.user = self.request.user
        character_goal.character = goal
        character_goal.save()
        return redirect("detail_character", pk=goal.id)


class CharacterGoalsUpdateView(LoginRequiredMixin, UpdateView):
    model = CharacterGoal
    template_name = "goals/update_character_goal.html"
    fields = ["name", "description", "character", "is_completed"]

    def get_success_url(self):
        return reverse_lazy("detail_character", args=[self.object.character_id])

class CharacterGoalsCompletedUpdateView(LoginRequiredMixin, UpdateView):
    model = CharacterGoal
    template_name = "goals/update_goal_complete.html"
    fields = ["is_completed"]

    def get_success_url(self):
        return reverse_lazy("detail_character", args=[self.object.character_id])

class CharacterGoalsDeleteView(LoginRequiredMixin, DeleteView):
    model = CharacterGoal
    template_name = "goals/delete_character_goal.html"
    context_object_name = "goal_delete"

    def get_success_url(self):
        return reverse_lazy("detail_character", args=[self.object.character_id])