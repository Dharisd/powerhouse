from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from .models import Payment
# Create your views here.



class PaymentListView(ListView):
    template_name = "index.html"
    context_object_name = "payments"

    def get_queryset(self):
        """return all unapproved  payments"""
        return Payment.objects.filter(payment_status="PENDING")





class PaymentDetailView(DetailView):
    model = Payment
    context_object_name = "payment"

    template_name =  "detail_view.html"

