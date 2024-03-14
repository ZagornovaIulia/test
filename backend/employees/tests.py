from decimal import Decimal
from django.test import TestCase
from django.urls import reverse

from orders.models import Product, Order
from clients.models import Client
from employees.models import Employee
from employees.serializers import EmployeeStatisticSerializer
from rest_framework.test import APIRequestFactory


class SerializerEmployeeTestCase(TestCase):
    def setUp(self) -> None:
        self.employee = Employee.objects.create(
            full_name='John Doe', birthdate='1990-01-01')
        self.test_client = Client.objects.create(
            full_name='Iu Zag', birthdate='1999-01-01')
        self.product = Product.objects.create(price=50)
        self.order = Order.objects.create(
            price=100, date='2024-04-08', client=self.test_client, employee=self.employee, product=self.product)
        return super().setUp()

    def test_serializer(self):
        serializer = EmployeeStatisticSerializer(self.employee)
        self.assertEqual(serializer.data, {'id': self.employee.id, 'full_name': self.employee.full_name, 'total_clients_count': 1,
                         'total_products_count': 0, 'total_sale_amount': Decimal('100')})

    def test_serializer_with_new_order(self):
        client = Client.objects.create(
            full_name='Daf', birthdate='1999-01-01')
        Order.objects.create(
            price=100, date='2024-04-08', client=client, employee=self.employee, product=self.product)
        serializer = EmployeeStatisticSerializer(self.employee)
        self.assertEqual(serializer.data, {'id': self.employee.id, 'full_name': self.employee.full_name, 'total_clients_count': 2,
                         'total_products_count': 0, 'total_sale_amount': Decimal('200')})
