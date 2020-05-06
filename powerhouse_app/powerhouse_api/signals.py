from .models import ChargingType,MeterBoard,MeterReading,MeterBill,Payment
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=MeterReading)
def createMeterBill(sender,instance, created, **kwargs):
    if created:
        meterreading = instance
        meterboard = meterreading.reading_meterboard
        reading_month = meterreading.reading_month
        
        # get the previous month from db
        '''
        fetching the previous months payment can be done by
        geting allpayments lower than the current month 
        '''
        try:
            last_reading = MeterReading.objects.filter(
                reading_meterboard= meterboard,
                reading_month__lt = reading_month,
            ).order_by('-reading_month')[0]
        
        except:
            print("exception occured")
            return "didnt create"

        '''
        creates a Meter bill if last reading exists
        '''

        #generates a bill_id in the format 1D_20200401 
        meterboard_number = meterboard.board_number
        meterboard_chargingtype = meterboard.board_type.name_shortform
        
        reading_date_formatted = reading_month.strftime("%Y%m")
        generated_bill_id = "{} {} {}".format(
            meterboard_number,
            reading_date_formatted,
            meterboard_chargingtype)

        generated_bill = MeterBill.objects.create(
            bill_id=generated_bill_id,
            billing_meterboard=meterboard,
            billing_start_reading=last_reading,
            billing_end_reading=meterreading,
            billing_month=reading_month.replace(day=1),
            bill_chargingtype= meterboard.board_type
        )
        generated_bill.save()
        return "success"


