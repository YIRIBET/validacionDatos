from django.urls import include, path
from .views import *
from django.contrib.auth.views import LogoutView
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = SimpleRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
path('',include(router.urls)),
path('token/', CustomTokenObtainPairView.as_view(), name='token'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]