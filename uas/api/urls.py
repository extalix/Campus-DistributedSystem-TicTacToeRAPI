from django.urls import path
from . import views

urlpatterns = [
    path('room/get', views.give_room, name="getRoomId"),
    path('room/<int:roomId>', views.get_room_stats, name="getRoomDetail"),
    path('room/<int:roomId>/score', views.get_room_score, name="getRoomScore"),
    path('room/<int:roomId>/stats', views.get_room_stats, name="getRoomStats"),
    path('room/<int:roomId>/opponent', views.get_other_player, name="getOpponent"),
]
