from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SalesAnalyticsSerializer
from api.models import Bill

class SalesAnalyticsAPIView(APIView):
    def get(self, request):
        max_sales_employee = Bill.objects.values('employee').annotate(total_sales=Sum('total_amount')).order_by('-total_sales').first()
        
        most_sold_product = Bill.objects.values('product').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity').first()
        
        serializer = SalesAnalyticsSerializer({
            'employee_name': max_sales_employee['employee'],
            'total_sales': max_sales_employee['total_sales'],
            'most_sold_product': most_sold_product['product'],
        })
        return Response(serializer.data)