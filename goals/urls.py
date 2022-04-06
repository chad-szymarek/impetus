from django.urls import path

from goals.views import CharacterGoalsCreateView
urlpatterns = [
    path("create/", CharacterGoalsCreateView.as_view(), name="create_character_goal")
]