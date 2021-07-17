from django.db import models

# Create your models here.
class Client(models.Model):
    fullname = models.CharField(max_length=50)
    nit = models.CharField(max_length=14, default="0")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname


class PaymentMethod(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("PD", "Pendiente"),
        ("PG", "Pagado"),
        ("EL", "Eliminado"),
    ]

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="PD")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    date = models.DateTimeField()
    stay_days = models.IntegerField(default=1)
    paid_amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.client.fullname} {self.date}"
