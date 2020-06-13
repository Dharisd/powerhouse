from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from ..models import Payment,MeterBill
from ..forms import PaymentStatusChangeForm
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect



def approve_bill(request):

    if request.method == "POST":
        form = PaymentStatusChangeForm(request.POST or None)

        if  form.is_valid():

            payment_uuid = form.cleaned_data["payment_uuid"]
            #gets the payment
            selected_payment = Payment.objects.get(pk = payment_uuid)

            if selected_payment:
                action = form.cleaned_data["action"]
                #change the payemnt properties if found
                selected_payment.payment_status = action

                #if approved update bill too
                if action == "APPROVED":
                    selected_payment.payment_bill.bill_status = "PAID"
                    selected_payment.payment_bill.save()

                selected_payment.save()
            
                return HttpResponseRedirect(selected_payment.get_absolute_url())

        return HttpResponseRedirect(selected_payment.get_absolute_url())

    