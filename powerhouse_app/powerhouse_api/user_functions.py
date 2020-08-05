from .models import ChargingType,MeterBoard,MeterReading,MeterBill,Payment
from .db_functions import getUsage



def getUserData(user):
    user_meterboards = MeterBoard.objects.filter(board_owner=user)
    meterboard_data = []

    for meterboard in user_meterboards:
        last_usage = getUsage(meterboard,MeterBill)

        # check for unpaid bills
        unpaid_bills_check = MeterBill.objects.filter(
            billing_meterboard=meterboard,
            bill_status="UNPAID")

        if len(unpaid_bills_check) > 0:
            unpaid_bills = True
        else:
            unpaid_bills = False

        generated_data = {
            "board_number": meterboard.board_number,
            "board_name": meterboard.board_name,
            "board_type": meterboard.board_type.name,
            "last_usage":last_usage,
            "unpaid_bills":unpaid_bills,
        }

        meterboard_data.append(generated_data)

    
    return meterboard_data

#returns all the unpaid bills for given metrboard
def getUserBills(meterboard_number):
    meterboard = MeterBoard.objects.get(board_number=meterboard_number)
    bill_data = []

    # check for unpaid bills
    bills = MeterBill.objects.filter(
        billing_meterboard=meterboard,
       ).order_by('-billing_month')

    for bill in bills:
        bill_data.append(bill.getDetails())


    return bill_data


#returns all the unpaid bills for given metrboard
def getUserUnpaidBills(meterboard_number):
    meterboard = MeterBoard.objects.get(board_name=meterboard_number)
    bill_data = []

    # check for unpaid bills
    unpaid_bills = MeterBill.objects.filter(
        billing_meterboard=meterboard,
        bill_status="UNPAID")

    for unpaid_bill in unpaid_bills:
        bill_data.append(unpaid_bill.getDetails())


    return bill_data
