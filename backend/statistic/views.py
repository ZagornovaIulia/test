from clients.models import Client
from clients.serializers import ClientStatisticSerializer
from employees.models import Employee
from employees.serializers import EmployeeStatisticSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


class StatisticEmployee(APIView):
    def get(self, request, format=None, id=None):
        obj = Employee.objects.get(id=id)
        serializer = EmployeeStatisticSerializer(
            obj, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatisticClient(APIView):
    def get(self, request, format=None, id=None):
        obj = Client.objects.get(id=id)
        serializer = ClientStatisticSerializer(
            obj, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
