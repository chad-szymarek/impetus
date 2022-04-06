from tkinter import W
from django.contrib import admin

from games.models import Game, Character, CharacterGoal

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    pass

class CharacterAdmin(admin.ModelAdmin):
    pass

class CharacterGoalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterGoal, CharacterGoalAdmin)