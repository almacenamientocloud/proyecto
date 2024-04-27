from.models import Employee
from rest_framework import serializers

class EmpleadoSerialezers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','identification','name','last_name','email','salary','is_active')

# read_only_fields = ('id')        
