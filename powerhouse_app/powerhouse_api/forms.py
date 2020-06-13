from django import forms
from django.forms import ModelForm
from .models import MeterReading 


class PaymentStatusChangeForm(forms.Form):

    payment_uuid = forms.CharField(label="payment_uuid",max_length=50)
    action = forms.CharField(label="action", max_length=10) # maybe should put choices here



class MeterReadingForm(ModelForm):
    class Meta:
        model = MeterReading
        fields = ["reading_meterboard","reading_month","reading_units","reading_datetime","reading_user"]