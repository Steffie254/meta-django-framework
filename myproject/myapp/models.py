from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# Create model DrinksCategory 


class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


# Create model Drinks
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
