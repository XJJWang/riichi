from django.contrib import admin

from .models import Game, Player


class GameAdmin(admin.ModelAdmin):
    list_display = (Game.view_players_scores, 'date')


admin.site.register(Game, GameAdmin)
admin.site.register(Player)
