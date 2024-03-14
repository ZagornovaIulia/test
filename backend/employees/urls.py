from django.urls import include, path
from employees.views import EmployeeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('', include(router.get_urls()))
]
