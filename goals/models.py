from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class CharacterGoal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    character = models.ForeignKey("games.Character", related_name="goals", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("detail_character", kwargs={"pk": self.pk})