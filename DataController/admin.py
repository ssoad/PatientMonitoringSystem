from django.contrib import admin
from .models import HeartRate, BloodPressure, Temperature, Humidity

# Register your models here.
admin.site.register([HeartRate, BloodPressure, Temperature, Humidity ])
