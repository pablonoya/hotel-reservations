from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Client, Reservation, PaymentMethod
from .serializers import (
    ClientSerializer,
    ReservationSerializer,
    PaymentMethodSerializer,
)

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(is_active=True).order_by("fullname")
    serializer_class = ClientSerializer

    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        client.is_active = False
        client.save()

        return Response(
            status=status.HTTP_200_OK,
            data={"detail": "deleted successfully"},
        )


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.filter(is_active=True)
    serializer_class = PaymentMethodSerializer

    def destroy(self, request, *args, **kwargs):
        payment_method = self.get_object()
        payment_method.is_active = False
        payment_method.save()

        return Response(
            status=status.HTTP_200_OK,
            data={"detail": "deleted successfully"},
        )


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.exclude(status="EL").order_by("date")
    serializer_class = ReservationSerializer

    def retrieve(self, request, pk=None):
        queryset = Reservation.objects.all()
        reservation = get_object_or_404(queryset, pk=pk)
        serializer = ReservationSerializer(reservation)

        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Reservation.objects.all()
        reservation = get_object_or_404(queryset, pk=pk)
        serializer = ReservationSerializer(reservation, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()
        reservation.status = "EL"
        reservation.save()

        return Response(
            status=status.HTTP_200_OK,
            data={"detail": "deleted successfully"},
        )
