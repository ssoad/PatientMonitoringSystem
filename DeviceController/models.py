from django.db import models


# Create your models here.
class Device(models.Model):
    DEVICE_NAME = models.CharField(max_length=200, blank=False, default="hospital_device")
    IP_ADDRESS = models.GenericIPAddressField(blank=False)
    LOCATION = models.CharField(max_length=100, blank=False)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.ip_address = None

    def __str__(self):
        return str(self.DEVICE_NAME+" : "+self.ip_address)
