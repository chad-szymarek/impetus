from django.contrib import admin

from goals.models import CharacterGoal

# Register your models here.


class CharacterGoalAdmin(admin.ModelAdmin):
    pass



admin.site.register(CharacterGoal, CharacterGoalAdmin)
