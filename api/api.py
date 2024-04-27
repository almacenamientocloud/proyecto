from rest_framework import viewsets, permissions
from .models import Employee
from .serializers import EmpleadoSerialezers

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerialezers