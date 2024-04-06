from rest_framework import generics, status

from .models import Product, Customer, Employee, Bill
from .serializers import ProductSerializer, CustomerSerializer, EmployeeSerializer, BillSerializer, EmployeeLoginSerializer

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .authentication import CustomJWTAuthentication

class ProductList(generics.ListAPIView):
	serializer_class = ProductSerializer
	authentication_classes = [CustomJWTAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		query_set = Product.objects.all()
		return query_set

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
	authentication_classes = [CustomJWTAuthentication]
	permission_classes = [permissions.IsAuthenticated]

class CustomerList(generics.ListCreateAPIView):
	serializer_class = CustomerSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		query_set = Customer.objects.all()
		return query_set

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()
	permission_classes = [permissions.IsAuthenticated]

class EmployeeSignUpView(generics.CreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		refresh = RefreshToken.for_user(user)
		return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeLoginView(generics.GenericAPIView):
    serializer_class = EmployeeLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Manual authentication
        try:
            employee = Employee.objects.get(username=username)
            if password == employee.password:
                refresh = RefreshToken.for_user(employee)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({"error": "Invalid username or passsword"}, status=status.HTTP_401_UNAUTHORIZED)
        except Employee.DoesNotExist:

            return Response({"error": "Employee Does Not Exist"}, status=status.HTTP_401_UNAUTHORIZED)

class CreateBillView(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Get data from request
        product_name = request.data.get('product_name')
        customer_name = request.data.get('customer_name')
        employee_username = request.data.get('employee_username')
        quantity = request.data.get('quantity', 1)  # Default to 1 if not provided
        
        
        try:
            product = Product.objects.get(productName=product_name)
        except Product.DoesNotExist:
            return Response({"error": f"Product with name '{product_name}' not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            customer = Customer.objects.get(CustomerName=customer_name)
        except Customer.DoesNotExist:
            return Response({"error": f"Customer with name '{customer_name}' not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            employee = Employee.objects.get(username=employee_username)
        except Employee.DoesNotExist:
            return Response({"error": f"Employee with username '{employee_username}' not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
        
        total_amount = product.price * int(quantity)
        
        
        bill_data = {
            'product': product.id,
            'customer': customer.id,
            'employee': employee.id,
            'quantity': quantity,
            'total_amount': total_amount,
            # date will be automatically added
        }
        serializer = self.get_serializer(data=bill_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
	
class ListBillsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer