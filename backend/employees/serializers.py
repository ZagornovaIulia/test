from employees.models import Employee
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.db.models import Sum
from clients.models import Client
from orders.filters import OrderFilter


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeStatisticSerializer(ModelSerializer):
    total_clients_count = serializers.SerializerMethodField()
    total_products_count = serializers.SerializerMethodField()
    total_sale_amount = serializers.SerializerMethodField()

    def get_total_clients_count(self, obj):
        orders = obj.orders.all()
        if request := self.context.get('request'):
            orders = OrderFilter(data=request.query_params, queryset=orders).qs
        return Client.objects.filter(orders__in=orders).count()

    def get_total_products_count(self, obj):
        orders = obj.orders.all()
        if request := self.context.get('request'):
            orders = OrderFilter(data=request.query_params, queryset=orders).qs
        return orders.aggregate(Sum("product__quantity"))["product__quantity__sum"]

    def get_total_sale_amount(self, obj):
        orders = obj.orders.all()
        if request := self.context.get('request'):
            orders = OrderFilter(data=request.query_params, queryset=orders).qs
        return orders.aggregate(Sum("price"))["price__sum"]

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'total_clients_count',
                  'total_products_count', 'total_sale_amount')
