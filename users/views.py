from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, ValidationError
from django.contrib.auth import get_user_model, authenticate
from .serializers.common import UserSerializer
import jwt
from django.conf import settings
from datetime import datetime, timedelta

User = get_user_model()



class RegisterView(APIView):

    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            user = serialized_user.save()  

        
            exp_date = datetime.now() + timedelta(days=1)
            token = jwt.encode(
                {
                    "user_id": user.id,
                    "email": user.email,
                    "exp": exp_date.timestamp()
                },
                settings.SECRET_KEY,
                algorithm="HS256"
            )

            
            return Response({"user": serialized_user.data, "token": token}, status=201)
        
        return Response(serialized_user.errors, status=422)

User = get_user_model()

class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')  
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password) 
        if user is None:
            raise NotAuthenticated("Invalid credentials")  

    
        exp_date = datetime.now() + timedelta(days=1)
        token = jwt.encode(
            {
                "user_id": user.id,
                "email": user.email,
                "exp": exp_date.timestamp()
            },
            settings.SECRET_KEY,
            algorithm="HS256"
        )

        return Response({"message": "Login successful", "token": token})