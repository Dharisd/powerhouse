from django.db.models.signals import post_save
import datetime as dt

'''
generate bill details from a MeterBill instance
 '''

def getBillDetails(meterbill):
    bill_id = meterbill.bill_id
    meterboard_number = meterbill.billing_meterboard.board_number
    meterboard_name = meterbill.billing_meterboard.board_name

    #getthe values for billing start reading and end reading
    billing_start_reading = meterbill.billing_start_reading
    billing_end_reading = meterbill.billing_end_reading

    #get the amounts of units used 
    billing_start_units = billing_start_reading.reading_units
    billing_end_units = billing_end_reading.reading_units
    billing_units = billing_end_units - billing_start_units

    #get the dates for billing start reading and billing redaind
    billing_start_day = billing_start_reading.reading_datetime
    billing_end_day = billing_end_reading.reading_datetime
    billing_month = billing_end_reading.reading_month

    ''''
    try get to get bil amounts for different usage ranges
    the code below

    finds number of hundreds of units passed adds each hundred unit
    passed to array.and then adds the remainder to array 

    the array indexes are used to find the units passed for a particular 
    category and multiply by the units passed

    '''
    billing_type = meterbill.bill_chargingtype
    split_hundreds = []
    
    hundreds_no = int(billing_units // 100)
    leftover_units = billing_units%100

    #add all hundreds to array to be multiplied later by charging rates
    for x in range(0,hundreds_no):
        split_hundreds.append(100)

    split_hundreds.append(leftover_units)

    #always make sure that the array length is 4 so the next actions dont trhough exception
    if len(split_hundreds) < 4:
        diff = 4 - len(split_hundreds)
        for x in range(0,diff):
            split_hundreds.append(0)

    first_hundred_amount = split_hundreds[0] * billing_type.first_hundred_rate
    two_hundred_amount = split_hundreds[1] * billing_type.first_two_hundred_rate
    three_hundred_amount = split_hundreds[2] * billing_type.first_three_hundred_rate
    three_hundred_plus_amount = split_hundreds[3] * billing_type.three_hundred_plus_rate

    total_amount = first_hundred_amount + two_hundred_amount + three_hundred_amount + three_hundred_plus_amount

    bill_details = {
        "bill_id":bill_id,
        "meterboard_name":meterboard_name,
        "billing_month":billing_month,
        "start_date":billing_start_day,
        "end_date": billing_end_day,
        "start_unit":billing_start_units,
        "end_units":billing_end_units,
        "used_units":billing_units,
        "charging_type":billing_type.name,
        "charging_rates":{
            "0_100":billing_type.first_hundred_rate,
            "101_200":billing_type.first_two_hundred_rate,
            "201_300":billing_type.first_three_hundred_rate,
            "300_plus":billing_type.three_hundred_plus_rate
        },
        "charging_units":{
            "0_100":str(split_hundreds[0]),
            "101_200":str(split_hundreds[1]),
            "201_300":str(split_hundreds[2]),
            "300_plus":str(split_hundreds[3]),
            "total_amount":str(billing_units),            
        },
        "charging amounts":{
            "0_100":first_hundred_amount,
            "101_200":two_hundred_amount,
            "201_300":three_hundred_amount,
            "300_plus":three_hundred_plus_amount,
            "total_amount":total_amount            
        },
        "bill_status":meterbill.bill_status,
        "time_generated": dt.datetime.now()
    }


    return bill_details


def getUsage(meterboard,MeterBill):
    meterboard_usage = []
    bills = MeterBill.objects.filter(billing_meterboard=meterboard)[:12]

    for bill in bills:
        bill = bill.getDetails()
        used_units = bill["used_units"]
        bill_month = bill["billing_month"]
        meterboard_usage.append([used_units,bill_month])


    return meterboard_usage






if __name__ == "__main__":
    from .models import ChargingType,MeterBoard,MeterReading,MeterBill,Payment
    pass




