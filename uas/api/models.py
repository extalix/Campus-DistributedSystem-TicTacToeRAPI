from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

class game(models.Model):
    room_name = models.CharField(max_length=60)
    player_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1', blank=True, null=True)
    player_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2', blank=True, null=True)
    turn = models.IntegerField(default=1)
    c1 = models.IntegerField(default=0)
    c2 = models.IntegerField(default=0)
    c3 = models.IntegerField(default=0)
    c4 = models.IntegerField(default=0)
    c5 = models.IntegerField(default=0)
    c6 = models.IntegerField(default=0)
    c7 = models.IntegerField(default=0)
    c8 = models.IntegerField(default=0)
    c9 = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)