from django.db import models

# Create your models here.
class Car(models.Model):
    car_model = models.CharField(max_length=100, null=False, default="Null")
    car_price = models.IntegerField(null=False,default="Null")
    production_year = models.DateField(default="Null")
