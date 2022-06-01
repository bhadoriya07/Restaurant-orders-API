from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models

class Menu(models.Model):
    item_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField()
    plate_size = models.CharField(max_length=10)

    def __str__(self):
        return self.item_name