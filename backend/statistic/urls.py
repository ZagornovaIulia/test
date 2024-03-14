from django.urls import path

from .views import StatisticClient, StatisticEmployee

urlpatterns = [
    path('employee/<int:id>', StatisticEmployee.as_view(),
         name='statistic-employee'),
    path('client/<int:id>', StatisticClient.as_view(), name='statistic-client'),
]
