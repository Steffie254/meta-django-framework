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
    def __str__(self):
        return self.drink


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name