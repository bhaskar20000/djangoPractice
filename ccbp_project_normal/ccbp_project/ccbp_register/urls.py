from django.urls import path
from . import views

urlpatterns = [
    path("", views.registration_form),
    path("players/", views.player_list),  
]


