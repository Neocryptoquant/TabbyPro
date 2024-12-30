from django.contrib import admin
from .models import Tournament, Team, Adjudicator, Match

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'format', 'pairing_method', 'created_at')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'wins', 'speaker_points')

@admin.register(Adjudicator)
class AdjudicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'experience_level', 'availability')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'round_number', 'get_teams', 'adjudicator')

    def get_teams(self, obj):
        return ', '.join([team.name for team in obj.teams.all()])

    get_teams.short_description = 'Teams'