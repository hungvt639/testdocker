from django.db import models

# Create your models here.


class Hello(models.Model):
    head = models.CharField(max_length=100)
    context = models.CharField(max_length=100)