from django.contrib import admin

# Register your models here.
from .models import Client, Reservation, PaymentMethod

admin.site.register([Client, Reservation, PaymentMethod])
