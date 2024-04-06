from django.db import models


class Product(models.Model):
	productName = models.CharField(max_length=100, unique=True)
	price = models.IntegerField()
	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.productName
	
class Customer(models.Model):
	CustomerName = models.CharField(max_length=100, unique=True)
	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.CustomerName
	
class Employee(models.Model):
	username = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30)
	is_authenticated = True

	def __str__(self):
		return self.username

class Bill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
