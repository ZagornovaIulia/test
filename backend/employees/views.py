import django_filters
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from orders.models import Order
from .serializers import EmployeeStatisticSerializer
from django_filters.rest_framework import DjangoFilterBackend


class OrderFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(
        field_name='date', lookup_expr='year')
    month = django_filters.NumberFilter(
        field_name='date', lookup_expr='month')

    class Meta:
        model = Order
        fields = ['year', 'month']


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        qs = self.get_queryset()
        serializer = EmployeeStatisticSerializer(
            qs, many=True, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)
