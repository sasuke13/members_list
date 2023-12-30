from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
