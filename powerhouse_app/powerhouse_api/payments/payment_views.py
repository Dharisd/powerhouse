from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from ..models import Payment,MeterBill
from ..forms import PaymentStatusChangeForm
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

class PaymentListView(ListView):
    paginate_by = 50
    template_name = "payments/index.html"
    context_object_name = "payments"
    payment_statuses = ["APPROVED","PENDING","REJECTED"]




    def get_queryset(self):
        received_status = self.kwargs["payment_status"]

        if received_status.upper() in self.payment_statuses:  
            return Payment.objects.filter(payment_status=received_status.upper())

        #if empty return full
        return Payment.objects.all()
    

    #modify context to add returning page type
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        received_status = self.kwargs["payment_status"]
        context['payment_pagetype'] = "All"    

        if received_status.upper() in self.payment_statuses: 
            context['payment_pagetype'] = received_status

        return context
        







class PaymentDetailView(DetailView):
    model = Payment
    context_object_name = "payment"

    template_name =  "payments/detail_view.html"