# Generated by Django 4.0.3 on 2022-04-06 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_remove_character_goals_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactergoal',
            name='list',
        ),
        migrations.AddField(
            model_name='charactergoal',
            name='characer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='games.character'),
        ),
        migrations.DeleteModel(
            name='CharacterGoalList',
        ),
    ]