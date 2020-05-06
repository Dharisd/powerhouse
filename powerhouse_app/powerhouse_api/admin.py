from django.contrib import admin
from .models import ChargingType,MeterBoard,MeterReading,MeterBill,Payment


# Register your models here.
admin.site.register(ChargingType)
admin.site.register(MeterBoard)
admin.site.register(MeterReading)
admin.site.register(MeterBill)
admin.site.register(Payment)