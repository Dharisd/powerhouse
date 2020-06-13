from django.urls import path,include
from .payments.payment_functions import approve_bill
from .payments.payment_views import PaymentListView,PaymentDetailView
from .readings.reading_views import MeterBoardListView,MeterReadingDetailView
from .readings.reading_functions import add_reading


app_name="powerhouse_app"
urlpatterns = [
    #payment
    path('admin/payments/<slug:payment_status>/', PaymentListView.as_view(),name="list_payments"),
    path('admin/payment/details/<slug:pk>/', PaymentDetailView.as_view(),name="payment"),
    path('admin/payment/change_status/', approve_bill,name="change_status"),

    #readings
    path('admin/readings/', MeterBoardListView.as_view(),name="list_readings"),
    path('admin/readings/view/<slug:board_number>/', MeterReadingDetailView.as_view(),name="reading"),
    path('admin/readings/add/', add_reading,name="add_reading"),

    #auth
    path('accounts/', include('django.contrib.auth.urls')),



    
]
