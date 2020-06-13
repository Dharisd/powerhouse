from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from .models import Payment,MeterBill
from .forms import PaymentStatusChangeForm
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect











