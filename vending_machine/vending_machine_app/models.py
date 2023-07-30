# vending_machine_app/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
