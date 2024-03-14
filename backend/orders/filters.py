from django_filters import NumberFilter, FilterSet
from .models import Order


class OrderFilter(FilterSet):
    year = NumberFilter(field_name='date', lookup_expr='year')
    month = NumberFilter(field_name='date', lookup_expr='month')
    
    class Meta:
        model = Order
        fields = ['year', 'month']
