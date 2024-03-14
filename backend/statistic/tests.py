from django.test import TestCase
from django.urls import reverse

from orders.models import Product, Order
from clients.models import Client
from employees.models import Employee


class StatisticEmployeeTestCase(TestCase):
    def setUp(self) -> None:
        self.employee = Employee.objects.create(
            full_name='John Doe', birthdate='1990-01-01')
        self.test_client = Client.objects.create(
            full_name='Iu Zag', birthdate='1999-01-01')
        self.product = Product.objects.create(price=50)
        self.order = Order.objects.create(
            price=100, date='2024-04-08', client=self.test_client, employee=self.employee, product=self.product)

        return super().setUp()

    def test_api_with_order(self):
        resp = self.client.get(
            reverse('statistic-employee', kwargs={'id': self.employee.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {'id': self.employee.id, 'full_name': self.employee.full_name, 'total_clients_count': 1,
                                       'total_products_count': 0, 'total_sale_amount': 100.0})

    def test_api_with_new_client(self):
        client = Client.objects.create(
            full_name='Full name', birthdate='1999-01-01')
        product = Product.objects.create(price=50, quantity=3)
        Order.objects.create(
            price=200, date='2024-04-08', client=client, employee=self.employee, product=product)

        resp = self.client.get(
            reverse('statistic-employee', kwargs={'id': self.employee.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {'id': self.employee.id, 'full_name': self.employee.full_name, 'total_clients_count': 2,
                                       'total_products_count': 3, 'total_sale_amount': 300.0})


class StatisticClientTestCase(TestCase):
    def setUp(self) -> None:
        self.employee = Employee.objects.create(
            full_name='John Doe', birthdate='1990-01-01')
        self.test_client = Client.objects.create(
            full_name='Iu Zag', birthdate='1999-01-01')
        self.product = Product.objects.create(price=50)
        self.order = Order.objects.create(
            price=100, date='2024-04-08', client=self.test_client, employee=self.employee, product=self.product)

        return super().setUp()

    def test_api_with_order(self):
        resp = self.client.get(
            reverse('statistic-client', kwargs={'id': self.test_client.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
                         'id': self.test_client.id, 'full_name': self.test_client.full_name, 'total_products_count': 0, 'total_sale_amount': 100.0})

    def test_api_with_new_client(self):
        client = Client.objects.create(
            full_name='Full name', birthdate='1999-01-01')
        product = Product.objects.create(price=50, quantity=3)
        Order.objects.create(
            price=200, date='2024-04-08', client=client, employee=self.employee, product=product)

        resp = self.client.get(
            reverse('statistic-client', kwargs={'id': self.test_client.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
                         'id': self.test_client.id, 'full_name': self.test_client.full_name, 'total_products_count': 0, 'total_sale_amount': 100.0})
