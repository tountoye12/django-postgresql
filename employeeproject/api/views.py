from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view 

from .serializers import *

from user.models import User
from user.models import Group


# Create your views here.



@api_view(["GET"])
def home(request): 

    users = User.objects.all()
    userSerialiazer = UserSerializer(users, many=True)

    return Response(data = userSerialiazer.data)




