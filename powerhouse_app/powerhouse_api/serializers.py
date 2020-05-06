from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "payment_bill",
            "payment_amount",
            "payment_slip",
            "payment_type",
            "payment_datetime",
            "payment_created_by",
            "payment_creation_method",
            ]