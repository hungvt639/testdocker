from django.db import models

# Create your models here.


class Hello(models.Model):
    head = models.CharField(max_length=100)
    context = models.CharField(max_length=100)


class Nguoi(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)