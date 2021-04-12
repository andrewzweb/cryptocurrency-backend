from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')

def room(request, room_name):
    return render(request, 'dashboard/room.html', {
        'room_name': room_name
    })
