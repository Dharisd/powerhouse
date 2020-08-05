from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import MeterBoard,Payment
from django.http import JsonResponse
from .user_functions import getUserData,getUserUnpaidBills,getUserBills
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser

from .serializers import PaymentSerializer
# Create your views here.



class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):  
        print(request.user)      
        user = User.objects.get(pk=request.user.id)
        if user :
            user_data = {
                "message": "user found",
                "username":user.username,
                "meterboards":getUserData(user)
            }
        else:
            user_data = {
                "message": "user not found",
                "meterboards": []
            }
    
        return JsonResponse(user_data, safe=False)





class UserBillDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,meterboard_number):
        print(meterboard_number)
        bills = getUserBills(meterboard_number)

        return_data = {
            "message":"success",
            "bills":bills
        }

        return JsonResponse(return_data,safe=False)

    

    



class PaymentCreateView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = PaymentSerializer









    

