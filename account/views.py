from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SingUpSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    user = SingUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'] ,
                username = data['email'] ,
                password = make_password(data['password']),
            )
            return Response(
                {'details':'Your account registered susccessfully!' },
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                {'error':'This email already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(user.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user,many=False)
    return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != "":
        user.password = make_password(data['password'])

    user.save()
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)