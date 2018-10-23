from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField
    stock = models.IntegerField
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Client(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    givemeMorePoints = models.IntegerField
    def __str__(self):
        return self.name

class Sale(models.Model):
    date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField
    discount = models.DecimalField
    client = models.ForeignKey(Client, on_delete=None)
    product = models.ForeignKey(Product, on_delete=None)
    def __str__(self):
        return "A Sale"
