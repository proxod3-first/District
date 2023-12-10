from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect

from base.models import *
from base.forms import *
from .serializers import *
from base.api import serializers

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import authentication_classes, permission_classes


## Routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/new_room',
        'PUT /api/rooms/:id',
        'DELETE /api/rooms/:id'
    ]
    return Response(routes)


## Room
@api_view(['GET'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAuthenticated])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAuthenticated])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAuthenticated])
def createRoom(request):    
    room = RoomSerializer(request.POST or None)
    if room.is_valid():
        room.save()
    return redirect('getRooms')


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateRoom(request, id):
    room = Room.objects.get(id=id)
    room = RoomSerializer(request.PUT or None, instance=room)
    if room.is_valid():
        room.save()
    return redirect('getRooms')


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAuthenticated])
def deleteRoom(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect('getRooms')




## Topic 
@login_required
@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def getTopic(request, pk):
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(topic, many=False)
    return Response(serializer.data)




## User
@login_required
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



## Message
@login_required
@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def getMessage(request, pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)


########################################