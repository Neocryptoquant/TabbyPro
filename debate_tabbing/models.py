# ==========================
# MODELS (models.py)
# ==========================
from django.db import models
from django.utils.timezone import now
import random

# Tournament Model
class Tournament(models.Model):
    name = models.CharField(max_length=255)
    format = models.CharField(max_length=50, choices=[('BP', 'British Parliamentary'), ('AP', 'Asian Parliamentary')])
    pairing_method = models.CharField(max_length=50, choices=[('Random', 'Random'), ('Power', 'Power'), ('RoundRobin', 'Round Robin')])
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Team Model
class Team(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=255)
    wins = models.IntegerField(default=0)
    speaker_points = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

# Adjudicator Model
class Adjudicator(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='adjudicators')
    name = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=50, choices=[('Novice', 'Novice'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')])
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Match Model
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    round_number = models.IntegerField()
    teams = models.ManyToManyField('Team', related_name='matches')
    adjudicator = models.ForeignKey(Adjudicator, on_delete=models.SET_NULL, null=True, blank=True)
    result = models.JSONField(null=True, blank=True)  # Store detailed results as JSON

    def __str__(self):
        return f"Match {self.id}: Round {self.round_number} in {self.tournament}"

    @staticmethod
    def bp_pairing(teams):
        """
        Pair teams into groups of 4 for BP format.
        """
        random.shuffle(teams)  # Shuffle teams randomly
        pairings = []
        for i in range(0, len(teams), 4):
            if i + 4 <= len(teams):
                pairings.append(teams[i:i + 4])
        return pairings

    @staticmethod
    def round_robin_pairing(teams, round_number):
        """
        Generate round-robin pairings for BP style (groups of 4).
        """
        n = len(teams)
        if n % 4 != 0:
            raise ValueError("Number of teams must be divisible by 4 for BP format")
        rotated = teams[:]
        for _ in range(round_number):
            rotated = [rotated[0]] + rotated[1:][::-1]
        pairings = []
        for i in range(0, len(rotated), 4):
            pairings.append(rotated[i:i + 4])
        return pairings

# Result Model
class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='results')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()

    def __str__(self):
        return f"Result: {self.team} - {self.score}"
