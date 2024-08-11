from django.db import models

# Create your models here.


class EmployeeGroup(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self) -> str:
     return self.name

class Employee(models.Model):
  name = models.CharField(max_length=100)
  company = models.CharField(max_length=100, default = "IT")
  email = models.EmailField()
  title = models.CharField(max_length=100)
  mobile = models.CharField(max_length=15)
  #photo = models.ImageField(upload_to='photos/', null=True, blank=True)
  photo = models.CharField(max_length=200, null=True, blank=True)

  employee_groudId = models.ForeignKey(EmployeeGroup, on_delete= models.CASCADE)













'''

    {
      "id": "hdnhsm",
      "name": "Diallo Mamadou",
      "compagny": "Youtub",
      "email": "diallo@gmail.com",
      "title": "Youtuber",
      "mobile": "1545415",
      "photo": ,
      "employee_groudId": "1"
    }

    {
      "id": "1",
      "name": "Design"
    }


'''
