from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings

User = get_user_model()

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if not request.headers:
            return None
        
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        

        if not auth_header.startswith('Bearer'):
            return None  
        
        token = auth_header.replace('Bearer ', '')
        
        try:
            payload = jwt.decode(
                jwt=token, 
                key=settings.SECRET_KEY,
                algorithms=['HS256']
            )
            
            user = User.objects.get(id=payload['user_id'])
            
            return (user, token)
        except jwt.DecodeError:
            
            return None  
        except jwt.ExpiredSignatureError:
            
            raise AuthenticationFailed('Token has expired')
        except Exception as e:
            print(f"Authentication error: {e}")
            return None  