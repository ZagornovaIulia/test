from clients.models import Client
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from orders.filters import OrderFilter
from .models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientStatisticSerializer(ModelSerializer):
    total_products_count = serializers.SerializerMethodField()
    total_sale_amount = serializers.SerializerMethodField()

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
        model = Client
        fields = ('id', 'full_name', 'total_products_count',
                  'total_sale_amount')
