from django.urls import path
from .views import ProductList, ProductDetail, CustomerList, CustomerDetail, EmployeeListView, EmployeeSignUpView, EmployeeLoginView, CreateBillView, ListBillsView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
	path('product/', ProductList.as_view()),
	path('product/<int:pk>/', ProductDetail.as_view()),
	path('customer/', CustomerList.as_view()),
	path('customer/<int:pk>/', CustomerDetail.as_view()),
	path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('login/', EmployeeLoginView.as_view(), name='employee-login'),
    path('signup/', EmployeeSignUpView.as_view(), name='employee-signup'),
	path('bill/create', CreateBillView.as_view(), name='add-bill'),
	path('bill/view', ListBillsView.as_view(), name='view-bill'),
	path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
