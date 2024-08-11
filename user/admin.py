from django.contrib import admin

# Register your models here.

from user.models import Employee, EmployeeGroup


admin.site.register(Employee)
admin.site.register(EmployeeGroup)

