from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from ..models import MeterBoard,MeterReading
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect



class MeterBoardListView(ListView):
    template_name = "readings/index.html"
    context_object_name = "meterboards"
    paginate_by = 20
    
    model = MeterBoard


class MeterReadingDetailView(ListView):
    slug_field = "reading_meterboard__board_number"
    slug_url_kwarg = 'board_number'
    model = MeterReading 
    context_object_name = "readings"
    template_name = "readings/detail_view.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Readings from that board
        reading_board = self.kwargs["board_number"]
        context["board_number"] = reading_board
        context["board_details"] = MeterBoard.objects.get(pk=reading_board)
        context['readings'] = MeterReading.objects.filter(reading_meterboard=reading_board).order_by("-reading_month")
        return context




    



