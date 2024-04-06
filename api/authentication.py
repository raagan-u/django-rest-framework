from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from .models import Employee

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token['user_id']
        
        try:
            return Employee.objects.get(id=user_id)
        except Employee.DoesNotExist:
            raise InvalidToken('User not found')
