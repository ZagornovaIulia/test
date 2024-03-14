from django.test import TestCase
from employees.models import Employee
from clients.models import Client
from orders.models import Product
from orders.models import Order
from orders.filters import OrderFilter


class OrderFilterTestCase(TestCase):

    def test_filtering_orders(self):
        client = Client.objects.create(
            full_name='Full name', birthdate='1999-01-01')
        self.employee = Employee.objects.create(
            full_name='John Doe', birthdate='1999-01-01')
        product = Product.objects.create(price=50, quantity=3)
        self.order1 = Order.objects.create(
            price=200, date='2024-05-08', client=client, employee=self.employee, product=product)
        self.order2 = Order.objects.create(
            price=300, date='2024-03-08', client=client, employee=self.employee, product=product)
        self.order3 = Order.objects.create(
            price=400, date='2023-03-08', client=client, employee=self.employee, product=product)

        filtered_orders = OrderFilter(
            data={'year': 2024}, queryset=Order.objects.all()).qs
        self.assertEqual(len(filtered_orders), 2)
        
        filtered_orders_ids = filtered_orders.values_list('id', flat=True)
        self.assertEqual(set(filtered_orders_ids), set(
            [self.order1.id, self.order2.id]))
