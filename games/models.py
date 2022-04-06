from django.db import models
from django.forms import CharField
from django.urls import reverse_lazy

from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

RACE_CHOICES = (
    ('Elf', 'Elf'),
    ('Dwarf', 'Dwarf'),
)


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(USER_MODEL, related_name="games")
    image = models.URLField('Discord link image')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("show_games", kwargs={"pk": self.pk})

class Character(models.Model):
    summary = models.TextField()
    name = models.CharField(max_length=100)
    race = models.CharField(choices = RACE_CHOICES, max_length=200, default='Elf')
    playersclass = models.CharField(max_length=50)
    user = models.ForeignKey(USER_MODEL, related_name="characters", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", related_name="characters", on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("show_games", kwargs={"pk": self.pk})

class CharacterGoal(models.Model):
    goal = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    characer = models.ForeignKey("Character", related_name="goals", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
        


