"""
URL configuration for tabbing_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
