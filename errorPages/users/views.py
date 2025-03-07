from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from .serializers import *
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer

#hacer las vistas de api_rest de usuarios 
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]
    #si quieres agregar la parte de seguridad 
    #pon estas dos variables
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #que metodos va a proteger 
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []
    

# hacer una vista que me devuelva mi token 
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer