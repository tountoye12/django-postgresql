from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status

from .serializers import EmployeeSerializer, GroupSerializer

from user.models import Employee
from user.models import EmployeeGroup


# Create your views here.



@api_view(["GET"])
def getAll(request): 
    employees = Employee.objects.all()
    employeesSerilizer = EmployeeSerializer(employees, many=True)
    return Response(employeesSerilizer.data)


@api_view(["POST"])
def addUser(request):
    serializer = EmployeeSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        print("Saving:", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Validation Errors:", serializer.errors)
        return Response({"msg": "Not valid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




