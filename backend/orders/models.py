from clients.models import Client
from django.db import models
from employees.models import Employee


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, related_name="orders")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="orders")
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="orders")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
