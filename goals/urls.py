from django.urls import path

from goals.views import CharacterGoalsCreateView, CharacterGoalsUpdateView,CharacterGoalsCompletedUpdateView,CharacterGoalsDeleteView
urlpatterns = [
    path("<int:goal_id>/create/", CharacterGoalsCreateView.as_view(), name="create_character_goal"),
    path("<int:pk>/update/", CharacterGoalsUpdateView.as_view(), name="update_character_goal"),
    path("<int:pk>/complete/", CharacterGoalsCompletedUpdateView.as_view(), name="complete_goal"),
    path("<int:pk>/delete/", CharacterGoalsDeleteView.as_view(), name="delete_goal"),

]