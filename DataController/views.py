import json
import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from DataController.models import HeartRate, BloodPressure, Temperature
from DeviceController.models import Device


def HeartRateData(request, ip):
    print(ip)
    devices = Device.objects.get(IP_ADDRESS=ip)
    heart_rate_labels = []
    heart_rate_data = []
    temp = []
    temp1 = []
    heart_data = HeartRate.objects.filter(DEVICE=devices)
    for ht in heart_data:
        temp.append(str(ht.DATETIME.time())[:8])
        temp1.append(ht.VALUE)
    for i in range(10):
        heart_rate_labels.append(temp.pop())
        heart_rate_data.append(temp1.pop())
    heart_rate_data.reverse()
    heart_rate_labels.reverse()
    heart_rate = {
        "labels": heart_rate_labels,
        "datasets": [
            {
                "data": heart_rate_data,
                "backgroundColor": "rgba(202, 201, 197, 0.9)",
                "borderColor": "rgba(190, 220, 220, 1)",
                "pointBackgroundColor": "rgba(35, 78, 123, 0.69)",
                "pointBorderColor": "#fff",
                "label": "Heart Rate Data",
                "name": "Heart Rate Data"
            }
        ]
    }
    dic = {
        "heart_rate": heart_rate,
    }
    # data = serialize("json", dic.all())
    # data1={}
    # for d in data:
    #     print(type(d))
    # data1[d['pk']] = d['fields']
    print()
    return HttpResponse(json.dumps(dic), content_type="application/json")


def BloodPressureData(request, ip):
    devices = Device.objects.get(IP_ADDRESS=ip)
    blood_pressure_labels = []
    blood_pressure_data = []
    temp = []
    temp1 = []
    heart_data = BloodPressure.objects.filter(DEVICE=devices)
    j = 0
    for ht in heart_data:
        temp.append(str(ht.DATETIME.time())[:8])
        temp1.append(ht.VALUE)
        j = j + 1
    for i in range(10):
        if j > i:
            blood_pressure_labels.append(temp.pop())
            blood_pressure_data.append(temp1.pop())
        else:
            break
    blood_pressure_data.reverse()
    blood_pressure_labels.reverse()
    blood_pressure = {
        "labels": blood_pressure_labels,
        "datasets": [
            {
                "data": blood_pressure_data,
                "backgroundColor": "rgba(255, 129, 17, 0.56)",
                "borderColor": "rgba(255, 129, 17, 1)",
                "pointBackgroundColor": "rgba(255, 73, 33, 1)",
                "pointBorderColor": "#fff",
                "label": "Blood Pressure Data",
                "name": "Blood Pressure Data"
            }
        ]
    }
    dic = {
        "blood_pressure": blood_pressure,
    }
    # data = serialize("json", dic.all())
    # data1={}
    # for d in data:
    #     print(type(d))
    # data1[d['pk']] = d['fields']
    print()
    return HttpResponse(json.dumps(dic), content_type="application/json")


@csrf_exempt
def saveData(request):
    if request.method == 'POST':
        ip = request.POST.get('ip_address')
        heart_rate_data = request.POST.get('heart_rate')
        blood_pressure_data = request.POST.get('blood_pressure')
        temperature_data = request.POST.get('temperature')
        datetime_now = datetime.datetime.now()
        device = Device.objects.get(IP_ADDRESS=ip)
        heart_rate = HeartRate(DEVICE=device, VALUE=heart_rate_data, DATETIME=datetime_now)
        heart_rate.save()
        blood_pressure = BloodPressure(DEVICE=device, VALUE=blood_pressure_data, DATETIME=datetime_now)
        blood_pressure.save()
        temperature = Temperature(DEVICE=device, VALUE=temperature_data, DATETIME=datetime_now)
        temperature.save()
        return HttpResponse(json.dumps({"status": "OK"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"default": "200"}), content_type="application/json")


import asyncio
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from time import sleep


@sync_to_async
def crunching_stuff():
    sleep(10)
    print("Woke up after 10 seconds!")


async def index(request):
    json_payload = {
        "message": "Hello world"
    }
    """
    or also
    asyncio.ensure_future(crunching_stuff())
    loop.create_task(crunching_stuff())
    """
    asyncio.create_task(crunching_stuff())
    return JsonResponse(json_payload)
