from rest_framework import serializers
from .models import Client, Reservation, PaymentMethod


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "fullname", "nit", "is_active"]


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ["id", "name", "is_active"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "id",
            "status",
            "client",
            "date",
            "stay_days",
            "payment_method",
            "paid_amount",
        ]
