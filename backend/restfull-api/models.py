from django.db import models

class User(models.Model):
    username = models.CharField(max_length=55)
    age = models.IntegerField()