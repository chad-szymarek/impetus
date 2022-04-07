from django.db import models
from django.forms import CharField
from django.urls import reverse_lazy

from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

CLASS_CHOICES = [
    ('Artificer', 'Artificer'),
    ('Barbarian', 'Barbarian'),
    ('Bard', 'Bard'),
    ('Cleric', 'Cleric'),
    ('Druid', 'Druid'),
    ('Fighter', 'Fighter'),
    ('Monk', 'Monk'),
    ('Paladin', 'Paladin'),
    ('Ranger', 'Ranger'),
    ('Rogue', 'Rogue'),
    ('Sorcerer', 'Sorcerer'),
    ('Warlock', 'Warlock'),
    ('Wizard', 'Wizard'),
]


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(USER_MODEL, related_name="games")
    user = models.ForeignKey(USER_MODEL, related_name="created_games", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("show_games", kwargs={"pk": self.pk})

class Character(models.Model):
    summary = models.TextField()
    name = models.CharField(max_length=100)
    playersclass = models.CharField(choices=CLASS_CHOICES, max_length=50, default='Artificer')
    user = models.ForeignKey(USER_MODEL, related_name="characters", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", related_name="characters", on_delete=models.CASCADE)


    def __str__(self):
        return self.name


        


