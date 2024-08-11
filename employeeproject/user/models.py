from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=256)
    compagny = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    mobile = models.CharField(max_length=256)
    photo = models.CharField(max_length=256)
    groudId = models.CharField(max_length=10)


class Group(models.Model):
    name = models.CharField(max_length=200)





'''

    {
      "id": "hdnhsm",
      "name": "Diallo Mamadou",
      "compagny": "Youtub",
      "email": "diallo@gmail.com",
      "title": "Youtuber",
      "mobile": "1545415",
      "photo": ,
      "groupId": "1"
    }

    {
      "id": "1",
      "name": "Design"
    }


'''
