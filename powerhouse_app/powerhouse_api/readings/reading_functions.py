from ..models import MeterReading,User
from ..forms import MeterReadingForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def add_reading(request):
    if request.method == "POST":
        form = MeterReadingForm(request.POST or None)
        print(form.errors)

        if form.is_valid():
            print("valids")

            #if valid send to where it came from
            form.save()
            board_number = request.POST["reading_meterboard"]
            return HttpResponseRedirect(reverse(f"powerhouse_app:reading", kwargs={'board_number': board_number}))
        #if invalid send to index of boards
    return HttpResponseRedirect(reverse("powerhouse_app:list_readings"))



#TODO
#add messages 