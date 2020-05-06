from django.db import models
import uuid
from django.contrib.auth.models import User
from .db_functions import getBillDetails,getUsage

# Create your models here.

class ChargingType(models.Model):
    name = models.CharField(max_length=200)
    name_shortform = models.CharField(max_length=5,null=True)

    '''
    first_hundred_rate: rate for units from 0 to a 200 
    first_two_hundred_rate: rate for units from 100 to 200
    first_three_hundred_rate: rate for units from 200 to 300
    three_hundred_plus_rate: for usage above 300 '''
    
    first_hundred_rate = models.DecimalField(max_digits=5, decimal_places=2)
    first_two_hundred_rate = models.DecimalField(max_digits=5, decimal_places=2)
    first_three_hundred_rate = models.DecimalField(max_digits=5, decimal_places=2)
    three_hundred_plus_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self): 
        return self.name



class MeterBoard(models.Model):
    #board identifiers
    board_name = models.CharField(max_length=200)
    board_number = models.IntegerField(primary_key=True)
    board_type = models.ForeignKey(ChargingType, on_delete=models.CASCADE)

    #connecting to owner
    board_owner = models.ManyToManyField(User)



    def __str__(self):

        return self.board_name


class MeterReading(models.Model):
    #the data about the reading
    reading_meterboard = models.ForeignKey(MeterBoard, on_delete=models.CASCADE)
    reading_month = models.DateField()
    reading_units = models.IntegerField()

    #the meta data about the reading
    reading_datetime = models.DateTimeField()
    reading_user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        #data to create unique identifer
        metreboard_number = self.reading_meterboard.board_number
        metreboard_type = self.reading_meterboard.board_type.name_shortform
        reading_date_formatted = self.reading_month.strftime("%Y%m%d")
        
        reading_identifier = "{}{}_{}".format(metreboard_number,metreboard_type,reading_date_formatted)
        return reading_identifier




class MeterBill(models.Model):

    billing_meterboard = models.ForeignKey(MeterBoard, on_delete=models.CASCADE)
    billing_month = models.DateField()

    #set through the set genbill function
    bill_id = models.CharField(max_length=50, primary_key=True)

    billing_start_reading = models.ForeignKey(MeterReading,related_name='%(class)s_starting_reading', on_delete=models.CASCADE)
    billing_end_reading = models.ForeignKey(MeterReading,related_name='%(class)s_ending_reading', on_delete=models.CASCADE)
    bill_chargingtype = models.ForeignKey(ChargingType ,null=True, on_delete=models.CASCADE)
    ''' 
    bill amount will be kept in model but the rates
    between hundreds will not be kept, and will be derived from the
    MetreBoard ChargingType and billing_start_reading and billing_end_reading
    '''


    PAID = "PAID"
    UNPAID = "UNPAID"
    BILL_STATUS_CHOICES = [
        (PAID, "PAID"),
        (UNPAID, "UNPAID")
    ]
    bill_status = models.CharField(
        max_length=6,
        choices= BILL_STATUS_CHOICES,
        default= UNPAID,
    )

    def getDetails(self):
        return getBillDetails(self)

    def __str__(self):
        return self.bill_id




class Payment(models.Model):
    
    payment_bill = models.ForeignKey(MeterBill,on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_slip = models.ImageField(upload_to="slips",blank=True,null=True)

    ONLINE = "ONLINE"
    CASH = "CASH"

    PAYMENT_TYPE_CHOICES = [
        (ONLINE, "ONLINE"),
        (CASH,"CASH")
    ]
    payment_type = models.CharField(
        max_length=6,
        choices=PAYMENT_TYPE_CHOICES,
        default= ONLINE
    )

    payment_identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_datetime = models.DateTimeField()
    payment_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    #statuses the payment can be in
    APPROVED = "APPROVED"
    PENDING = "PENDING"

    PAYMENT_STATUSES = [
        (APPROVED,"APPROVED"),
        (PENDING,"PENDING"),

    ]

    payment_status = models.CharField(
        max_length = 8,
        choices= PAYMENT_STATUSES,
        default = APPROVED
    )

    AUTOGEN = "AUTOGEN"
    MANUAL = "MANUAL"

    PAYMENT_CREATION_METHODS = [
        (AUTOGEN, "AUTOGEN"),
        (MANUAL,"MANUAL")
    ]

    payment_creation_method = models.CharField(
        max_length = 8,
        choices = PAYMENT_CREATION_METHODS,
        default = AUTOGEN

    )

    def __str__(self):
        payment_bill_id = self.payment_bill.bill_id
        payment_uuild = self.payment_identifier

        return "{} {}".format(payment_bill_id,payment_uuild)

    
        def get_absolute_url(self):
            return reverse('powerhouse_api:payment', args=[str(self.pk)])






