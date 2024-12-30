# ==========================
# API VIEWS (views.py)
# ==========================
from rest_framework.generics import ListCreateAPIView
from .models import Tournament
from .serializers import TournamentSerializer
from rest_framework import views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Tournament, Match
from .serializers import MatchSerializer



class TournamentListView(ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class PairingView(views.APIView):
    def post(self, request, tournament_id):
        tournament = get_object_or_404(Tournament, id=tournament_id)
        teams = list(tournament.teams.all())
        round_number = request.data.get('round_number')

        if not round_number:
            return Response({"error": "Round number is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Determine pairing method based on tournament format and pairing method
            if tournament.format == 'BP':
                if tournament.pairing_method == 'RoundRobin':
                    rooms = Match.round_robin_pairing(teams, int(round_number))
                else:  # Default to random BP pairing
                    rooms = Match.bp_pairing(teams)
            else:
                return Response({"error": "Unsupported format for pairing."}, status=status.HTTP_400_BAD_REQUEST)

            # Save pairings to the database
            matches = []
            for room in rooms:
                match = Match.objects.create(
                    tournament=tournament,
                    round_number=round_number
                )
                match.teams.add(*room)
                matches.append(MatchSerializer(match).data)

            return Response({"matches": matches}, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
