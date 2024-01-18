from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'employees', views.EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns += router.urls

# companies/{id}/employees
