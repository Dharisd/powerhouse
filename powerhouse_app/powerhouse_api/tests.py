from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from .models import MeterBill,MeterReading,ChargingType,MeterBoard
from .db_functions import getUsage
from dateutil.relativedelta import *
from .user_functions import getUserData



# Create your tests here.
class MeterBoardTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="energy_user2",password="12345")
        test_type = ChargingType.objects.create(
            name="domestic",
            name_shortform="D",
            first_hundred_rate = 1.55,
            first_two_hundred_rate = 2.55,
            first_three_hundred_rate = 3.55,
            three_hundred_plus_rate = 6.55


        )
        self.test_meterboard = MeterBoard.objects.create(
            board_number=1,
            board_name="test_house1",
            board_type=test_type,
            )

        self.test_user.save()
        test_type.save()
        self.test_meterboard.board_owner.set([self.test_user])
        self.test_meterboard.save()
        



        '''
        adds one meter reading and checks if bills are generated for the readings 
        '''
    def test_are_bills_generated_for_one_reading(self):

        reading_one = MeterReading.objects.create(
            reading_meterboard=self.test_meterboard,
            reading_month= datetime.datetime(2020, 1, 1),
            reading_units=1500,
            reading_datetime=datetime.datetime.now(),
            reading_user= self.test_user
        )
        reading_one.save()

        generated_bills = MeterBill.objects.all()
        print(generated_bills)

        self.assertEqual(len(generated_bills),0)



    def test_are_bills_generated_for_two_readings(self):

        reading_one = MeterReading.objects.create(
            reading_meterboard=self.test_meterboard,
            reading_month= datetime.datetime(2020, 1, 1),
            reading_units=1500,
            reading_datetime=datetime.datetime.now(),
            reading_user= self.test_user
        )

        reading_two = MeterReading.objects.create(
            reading_meterboard=self.test_meterboard,
            reading_month= datetime.datetime(2020, 2, 1),
            reading_units=1900,
            reading_datetime=datetime.datetime.now(),
            reading_user= self.test_user
        )


        reading_one.save()
        reading_two.save()

        generated_bills = MeterBill.objects.all()
        print(generated_bills)

        self.assertEqual(len(generated_bills),1)




    def test_get_bill_details(self):

        reading_one = MeterReading.objects.create(
            reading_meterboard=self.test_meterboard,
            reading_month= datetime.datetime(2020, 1, 1),
            reading_units=1500,
            reading_datetime=datetime.datetime.now(),
            reading_user= self.test_user
        )

        reading_two = MeterReading.objects.create(
            reading_meterboard=self.test_meterboard,
            reading_month= datetime.datetime(2020, 2, 1),
            reading_units=1900,
            reading_datetime=datetime.datetime.now(),
            reading_user= self.test_user
        )


        reading_one.save()
        reading_two.save()

        generated_bill = MeterBill.objects.all()[0]
        generated_details = generated_bill.getDetails()
        #print(generated_details)

        self.assertEqual(type(generated_details),dict)



    
    def test_are_twelve_bills_for_a_year(self):
        usage = 100
        start_date = datetime.datetime(2020, 1, 1)

        for i in range(1,14):
            usage += 100
            start_date = start_date+relativedelta(months=+1)
            

            reading = MeterReading.objects.create(
                reading_meterboard=self.test_meterboard,
                reading_month= start_date,
                reading_units=usage,
                reading_datetime=datetime.datetime.now(),
                reading_user= self.test_user
            ) 
            reading.save()


        generated_bills = MeterBill.objects.all()
        for bill in generated_bills:
            print(bill.getDetails())
        print(generated_bills)

        self.assertEqual(len(generated_bills),12)




class MeterBoardTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="energy_user2",password="12345")
        test_type = ChargingType.objects.create(
            name="domestic",
            name_shortform="D",
            first_hundred_rate = 1.55,
            first_two_hundred_rate = 2.55,
            first_three_hundred_rate = 3.55,
            three_hundred_plus_rate = 6.55


        )
        self.test_meterboard = MeterBoard.objects.create(
            board_number=1,
            board_name="test_house1",
            board_type=test_type,
            )

        self.test_user.save()
        test_type.save()
        self.test_meterboard.board_owner.set([self.test_user])
        self.test_meterboard.save()

        usage = 100
        start_date = datetime.datetime(2020, 1, 1)

        for i in range(1,14):
            usage += 100
            start_date = start_date+relativedelta(months=+1)
            

            reading = MeterReading.objects.create(
                reading_meterboard=self.test_meterboard,
                reading_month= start_date,
                reading_units=usage,
                reading_datetime=datetime.datetime.now(),
                reading_user= self.test_user
            ) 
            reading.save()

        

        

    

        
    def test_get_twelve_month_usage(self):

        usage_array = getUsage(self.test_meterboard,MeterBill)
        print(usage_array)

        self.assertEqual(len(usage_array),12)



class UserTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="energy_user2",password="12345")
        test_type = ChargingType.objects.create(
            name="domestic",
            name_shortform="D",
            first_hundred_rate = 1.55,
            first_two_hundred_rate = 2.55,
            first_three_hundred_rate = 3.55,
            three_hundred_plus_rate = 6.55


        )
        self.test_meterboard = MeterBoard.objects.create(
            board_number=1,
            board_name="test_house1",
            board_type=test_type,
            )

        self.test_user.save()
        test_type.save()
        self.test_meterboard.board_owner.set([self.test_user])
        self.test_meterboard.save()

        usage = 100
        start_date = datetime.datetime(2020, 1, 1)

        for i in range(1,14):
            usage += 100
            start_date = start_date+relativedelta(months=+1)
            

            reading = MeterReading.objects.create(
                reading_meterboard=self.test_meterboard,
                reading_month= start_date,
                reading_units=usage,
                reading_datetime=datetime.datetime.now(),
                reading_user= self.test_user
            ) 
            reading.save()

    
    def test_user_return_data(self):
        home_data = getUserData(self.test_user)
        print(home_data)


        

            


