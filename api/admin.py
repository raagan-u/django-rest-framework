from django.contrib import admin
from .models import Product, Customer, Employee, Bill
# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Bill)