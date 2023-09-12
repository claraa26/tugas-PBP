from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    how_many_days = models.IntegerField()
    description = models.TextField()
# Create your models here.
