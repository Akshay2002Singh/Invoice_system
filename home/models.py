from cmath import phase
from django.db import models

# Create your models here.
class invoice_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    d_name = models.CharField(max_length=40)
    d_email = models.CharField(max_length=40)
    d_phone = models.IntegerField()
    d_address = models.CharField(max_length=50)
    d_items = models.TextField()
    d_catagoried = models.TextField()
    d_prices = models.TextField()
    d_quantities = models.TextField()

    def __str__(self):
        return f"{self.d_name} {self.id}"


