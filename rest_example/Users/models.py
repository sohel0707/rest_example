from django.db import models


class User(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    street = models.CharField(max_length=30)
    suite = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)