from dataclasses import field
from pyexpat import model
from rest_framework import serializers 
from api.models import Company, Employee


# create serilazers 
class CompanySerialiazer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerialiazer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'