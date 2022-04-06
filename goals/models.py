from django.db import models

# Create your models here.

class CharacterGoal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    characer = models.ForeignKey("games.Character", related_name="goals", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name