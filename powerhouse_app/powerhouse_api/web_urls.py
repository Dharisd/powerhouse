from django.urls import path
from .web_views import PaymentListView,PaymentDetailView


app_name="powerhouse_app"
urlpatterns = [
    path('', PaymentListView.as_view(),name="list_payments"),
    path('payment/details/<slug:pk>/', PaymentDetailView.as_view(),name="payment"),

    
]
