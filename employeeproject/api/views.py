from django.shortcuts import get_object_or_404
from  rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status


from .serializers import EmployeeSerializer, GroupSerializer

from user.models import Employee
from user.models import EmployeeGroup


# Create your views here.

@api_view(["GET"])
def get_all_employee(request): 
    employees = Employee.objects.all()
    employeesSerilizer = EmployeeSerializer(employees, many=True)
    return Response(employeesSerilizer.data)


@api_view(["POST"])
def add_user(request):
    serializer = EmployeeSerializer(data=request.data)
    #print(serializer)
    if serializer.is_valid():
        serializer.save()
        print("Saving:", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Validation Errors:", serializer.errors)
        return Response({"msg": "Not valid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)







# group views stats here

@api_view(["POST"])
def add_group(request):
    
    groupSerializer = GroupSerializer(data = request.data)

    if groupSerializer.is_valid():
        groupSerializer.save()

        return Response(groupSerializer.data, status=status.HTTP_201_CREATED)
    else: return Response({"msg": "Not valid data", "errors": groupSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_group(request):
    groups  = EmployeeGroup.objects.all()
    groupsSerializer = GroupSerializer(groups, many= True)
    return Response(groupsSerializer.data)



@api_view(["GET"])
def get_group(request, pk):
    emplpyeeGroup = get_object_or_404(EmployeeGroup, pk=pk)
    empployeGroupSerializer = GroupSerializer(emplpyeeGroup)
    return Response(empployeGroupSerializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_group(request, pk):
    employeeGroup = get_object_or_404(EmployeeGroup, pk= pk)
    employeeGroup.delete()
    return Response({"msg": "Deleted"}, status=status.HTTP_200_OK)