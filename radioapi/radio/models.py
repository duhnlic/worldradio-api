from django.db import models

class Radio(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    url = models.CharField(max_length=100)