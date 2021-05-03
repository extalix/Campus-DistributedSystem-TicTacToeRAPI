from django.http.response import HttpResponse, JsonResponse
from .models import game

def get_room_object(id):
    try:
        room = game.objects.get(pk=id)
        return room
    except game.DoesNotExist:
        return None

# Create your views here.
def get_room_stats(request, roomId):
    room = get_room_object(roomId)
    if not room:
        return JsonResponse({})

    context = {}
    context['turn'] = room.turn
    context['c1'] = room.c1
    context['c2'] = room.c2
    context['c3'] = room.c3
    context['c4'] = room.c4
    context['c5'] = room.c5
    context['c6'] = room.c6
    context['c7'] = room.c7
    context['c8'] = room.c8
    context['c9'] = room.c9

    return JsonResponse(context)

def get_room_score(request, roomId):
    room = get_room_object(roomId)
    if not room:
        return JsonResponse({})

    context = {}
    context['p1'] = room.score1
    context['p2'] = room.score2
    
    return JsonResponse(context)

def get_other_player(request, roomId):
    room = get_room_object(roomId)
    if not room:
        return JsonResponse({})

    context = {}
    if (room.player_one == request.user):
        context['a'] = request.user.username
        if (room.player_two) :
            context['b'] = room.player_two.username
    
    if (room.player_two == request.user):
        if (room.player_one):
            context['a'] = room.player_one.username
        context['b'] = request.user.username
        
    return JsonResponse(context)

def give_room(request):
    asPlayerOne = game.objects.filter(player_one=request.user).exclude(player_two=request.user)
    if (asPlayerOne):
        return JsonResponse({'roomId' : asPlayerOne[0].id})
    
    asPlayerTwo = game.objects.filter(player_two=request.user).exclude(player_one=request.user)
    if (asPlayerTwo):
        return JsonResponse({'roomId' : asPlayerTwo[0].id})

    available = game.objects.exclude(player_one__isnull=False, player_two__isnull=False)
    if (available):
        designated = available[0]
        if (designated.player_one):
            designated.player_two = request.user
        else:
            designated.player_one = request.user

        designated.save()
        return JsonResponse({'roomId' : designated.id})
    
    newRoom = game(room_name='Untitled', player_one=request.user)
    newRoom.save()
    return JsonResponse({'roomId' : newRoom.id})

def update_game(request, roomId):
    if (request.method == "POST"):
        room = get_room_object(roomId)
        room.c1 = request.POST['c1']
        room.c2 = request.POST['c2']
        room.c3 = request.POST['c3']
        room.c4 = request.POST['c4']
        room.c5 = request.POST['c5']
        room.c6 = request.POST['c6']
        room.c7 = request.POST['c7']
        room.c8 = request.POST['c8']
        room.c9 = request.POST['c9']
        if (room.turn == 1):
            room.turn = 2
        else:
            room.turn = 1
        room.save()

def end_round(request, roomId):
    if (request.method == "POST"):
        room = get_room_object(roomId)
        room.c1 = 0
        room.c2 = 0
        room.c3 = 0
        room.c4 = 0
        room.c5 = 0
        room.c6 = 0
        room.c7 = 0
        room.c8 = 0
        room.c9 = 0
        room.turn = 1

        if (request.POST['winner'] == 1):
            room.score1 += 1
        if (request.POST['winner'] == 2):
            room.score += 1
        
        room.save()
        return HttpResponse(200)
