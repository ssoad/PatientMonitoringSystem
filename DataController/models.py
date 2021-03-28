from django.db import models
from DeviceController.models import Device


# Create your models here.
class HeartRate(models.Model):
    DEVICE = models.ForeignKey(Device, on_delete=models.CASCADE)
    VALUE = models.FloatField(blank=False)
    DATETIME = models.DateTimeField(blank=False)

    def __str__(self):
        return str(str(self.DEVICE.IP_ADDRESS) + " : " + self.DEVICE.DEVICE_NAME + " : " + str(self.VALUE))


class BloodPressure(models.Model):
    DEVICE = models.ForeignKey(Device, on_delete=models.CASCADE)
    VALUE = models.FloatField(blank=False)
    DATETIME = models.DateTimeField(blank=False)

    def __str__(self):
        return str(str(self.DEVICE.IP_ADDRESS) + " : " + self.DEVICE.DEVICE_NAME + " : " + str(self.VALUE))


class Temperature(models.Model):
    DEVICE = models.ForeignKey(Device, on_delete=models.CASCADE)
    VALUE = models.FloatField(blank=False)
    DATETIME = models.DateTimeField(blank=False)

    def __str__(self):
        return str(str(self.DEVICE.IP_ADDRESS) + " : " + self.DEVICE.DEVICE_NAME + " : " + str(self.VALUE))
