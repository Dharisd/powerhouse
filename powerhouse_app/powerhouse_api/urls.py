from django.contrib import admin
from django.urls import path
from .views import UserDetailView,UserBillDetailView,PaymentCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/details/', UserDetailView.as_view(), name='get_user_details'),
    path('v1/bills/<int:meterboard_number>', UserBillDetailView.as_view(), name='get_unpaid_bills'),
    path('v1/token/obtain/', TokenObtainPairView.as_view(), name='token_create'),  
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/create/payment', PaymentCreateView.as_view(), name='create_payment'),
    
]
