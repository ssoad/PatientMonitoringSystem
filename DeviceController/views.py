import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from DeviceController.models import Device


def deviceList(request):
    devices = list(Device.objects.all())
    devices_list = []
    for device in devices:
        name = device.DEVICE_NAME
        ip = device.IP_ADDRESS
        location = device.LOCATION
        dic = {
            "pk": device.pk,
            "DEVICE_NAME": name,
            "IP_ADDRESS": ip,
            "LOCATION": location,
        }
        devices_list.append(dic)
    # devices_list = serializers.serialize("json", devices_list)
    # struct = json.loads(devices_list)
    context = {
        "devices": devices_list
    }
    return JsonResponse(context)


def deviceView(request):
    devices = Device.objects.all()
    context = {
        'devices': devices
    }
    return render(request, 'line_chart.html', context)
