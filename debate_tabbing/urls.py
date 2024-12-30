from django.contrib import admin
from django.urls import path
from debate_tabbing.views import TournamentListView, PairingView

import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponse

def debug_request(request, *args, **kwargs):
    logger.info(f"Received request: {request.path}")
    return HttpResponse("Debugging URL Configuration")

urlpatterns = [
    path('api/debug/', debug_request),  # Test if this works
    path('admin/', admin.site.urls),
    path('api/tournaments/', TournamentListView.as_view(), name='tournament-list'),
    path('api/tournaments/<int:tournament_id>/pairings/', PairingView.as_view(), name='pairings'),
]
