from django.contrib import admin

from games.models import Game, Character

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    pass

class CharacterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)
admin.site.register(Character, CharacterAdmin)