from rest_framework import serializers
from .models import Product, Customer, Employee, Bill

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields=('__all__')
	
class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields=('__all__')
	
class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'username', 'password')
	
	def create(self, data):
		return Employee.objects.create(**data)

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('product', 'customer', 'employee', 'quantity', 'date_added', 'total_amount')

class EmployeeLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            return data
        else:
            raise serializers.ValidationError("Username and password are required.")