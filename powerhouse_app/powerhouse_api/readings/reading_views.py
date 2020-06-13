from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from ..models import MeterBoard,MeterReading
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect



class MeterBoardListView(ListView):
    template_name = "readings/index.html"
    context_object_name = "meterboards"
    
    model = MeterBoard


class MeterReadingDetailView(ListView):
    slug_field = "reading_meterboard__board_number"
    slug_url_kwarg = 'board_number'
    model = MeterReading 
    context_object_name = "readings"
    template_name = "readings/detail_view.html"

    ordering = ["-reading_month"]



    



