from django.shortcuts import render
from django.views import generic

from apps.pages.forms import ServiceForm, TeamForm
from apps.pages.models import Service, Team


class ServiceListView(generic.ListView):
    model = Service
    template_name = 'service_list.html'


class TeamListView(generic.ListView):
    model = Team
    template_name = 'team_list.html'

