from rest_framework import serializers

class SalesAnalyticsSerializer(serializers.Serializer):
    employee_name = serializers.CharField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
    most_sold_product = serializers.CharField()