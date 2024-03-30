from django.db import models

class Book(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField()
     price = models.FloatField()
     count = models.IntegerField(default=1)
