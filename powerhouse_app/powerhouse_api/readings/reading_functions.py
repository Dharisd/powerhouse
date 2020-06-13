from ..models import MeterReading
from ..forms import MeterReadingForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def add_reading(request):
    if request.method == "POST":
        form = MeterReadingForm(request.POST or None)

        if form.is_valid():
            form.save()
            #if valid send to where it came from
            board_number = form["cleaned_data"]["board_number"]
            HttpResponseRedirect(reverse(f"powerhouse_app: reading '{board_number}'"))
        #if invalid send to index of boards
        HttpResponseRedirect(reverse("powerhouse_app: list_readings"))



#TODO
#add messages 