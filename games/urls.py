from django.urls import path
from games.views import (
    CharacterDetailView,
    GameListView,
    GameDetailView,
    GameCreateView,
    GameDeleteView,
    GameUpdateView,
    CharacterCreateView,
    CharacterDetailView,
    CharacterUpdateView
)

urlpatterns = [
    path("", GameListView.as_view(), name="list_games"),
    path("<int:pk>/", GameDetailView.as_view(), name="show_game"),
    path("create/", GameCreateView.as_view(), name="create_game"),
    path("<int:pk>/delete/", GameDeleteView.as_view(), name="delete_game"),
    path("<int:pk>/update/", GameUpdateView.as_view(), name="update_game"),


    path("<int:game_id>/character/create/", CharacterCreateView.as_view(), name="create_character"),
    path("character/<int:pk>/", CharacterDetailView.as_view(), name="detail_character"),
    path("character/<int:pk>/edit/", CharacterUpdateView.as_view(), name="update_character"),
]
