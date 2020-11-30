"""
smstest URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    #router.register(r'api', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/elements/', include("elements.api.urls")),
    path('api/commodity/', include("commodity.api.urls"),name='commodity-api'),
    path('api/chemical_composition/', include("chemical_composition.api.urls")),
]
