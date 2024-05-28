from django.urls import path

from apps.pages.views import ServiceListView, TeamListView


urlpatterns = [
    path('service/list', ServiceListView.as_view(), name="service_list"),
    path('team/list/', TeamListView.as_view(), name="team_list"),
]