

from rest_framework import serializers

from  user.models import Employee, EmployeeGroup

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeGroup
        fields = '__all__'