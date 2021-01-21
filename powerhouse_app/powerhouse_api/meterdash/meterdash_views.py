from django.views.generic import DetailView,ListView
from rest_framework.permissions import IsAuthenticated
from ..models import MeterBoard,MeterReading,MeterBill
from ..user_functions import getUserBills
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models.query_utils import Q
from .meterboard_filters import MeterBoardFilterSet
from ..forms import BasicSearchForm
from django.http import HttpResponse, HttpResponseRedirect



class MeterBoardDashListView(ListView):
    template_name = "meterdash/index.html"
    context_object_name = "meterboards"
    paginate_by = 10
    
    model = MeterBoard


#implement metersearch  based name or number
class MeterBoardSearchView(ListView):
    template_name = "meterdash/index.html"
    context_object_name = "meterboards"
    form_class = BasicSearchForm
    paginate_by = 10
    
    model = MeterBoard
    
    def get_queryset(self):
        self.form = self.form_class(self.request.GET)

        if self.form.is_valid():
            search_query = self.form.cleaned_data["search_query"] 
            board_number_filter = MeterBoard.objects.filter(board_number__icontains=search_query)
            board_name_filter = MeterBoard.objects.filter(board_name__icontains=search_query)
            return board_name_filter | board_number_filter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ex_query"] = self.form.cleaned_data["search_query"]
        context["current_page"] = "MeterBoard Search results"
        return context

class MeterBoardDashView(ListView):
    slug_field = "reading_meterboard__board_number"
    slug_url_kwarg = 'board_number'
    model = MeterReading 
    context_object_name = "readings"
    template_name = "meterdash/detail_view.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Readings from that board
        reading_board = self.kwargs["board_number"]
        bills = getUserBills(reading_board)

        context["current_page"] = "Dashboard"
        context["board_number"] = reading_board
        context["bills"]  = bills
        context["board_details"] = MeterBoard.objects.get(pk=reading_board)
        context['readings'] = MeterReading.objects.filter(reading_meterboard=reading_board).order_by("-reading_month")
        return context
