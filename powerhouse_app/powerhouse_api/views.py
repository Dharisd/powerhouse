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
        user = User.objects.get(pk=request.user.id)

        print(meterboard_number)
    

class PaymentListView(ListView):
    template_name = "index.html"
    context_object_name = "payments"

    def get_queryset(self):
        """return all unapproved  payments"""
        return Payment.objects.filter(payment_status="PENDING")
        meterboard = MeterBoard.objects.get(board_number=meterboard_number,board_owner=user)

        if meterboard:
            bills_data= {
                "message":"meterboard found",
                "bills":getUserBills(meterboard)
            }
    
        else:
            bills_data = {
                "message":"meterboard not found",
                "bills":[]
            }
        
        print(bills_data)

        return JsonResponse(bills_data,safe=False)
    



class PaymentCreateView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        serialized_data = PaymentSerializer(data=request.data)\

        if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)








    

