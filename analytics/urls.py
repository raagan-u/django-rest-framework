from django.urls import path
from .views import SalesAnalyticsAPIView

urlpatterns = [
    path('sales/', SalesAnalyticsAPIView.as_view(), name='sales-analytics'),
]