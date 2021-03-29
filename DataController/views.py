import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from DataController.models import HeartRate, BloodPressure
from DeviceController.models import Device


def HeartRateData(request, ip):
    print(ip)
    devices = Device.objects.get(IP_ADDRESS=ip)
    heart_rate_labels = []
    heart_rate_data = []
    heart_data = HeartRate.objects.filter(DEVICE=devices)
    i = 0
    for ht in heart_data:
        heart_rate_labels.append(str(ht.DATETIME.time()))
        heart_rate_data.append(ht.VALUE)
        i += 1
        if i > 9:
            break

    heart_rate = {
        "labels": heart_rate_labels,
        "datasets": [
            {
                "data": heart_rate_data,
                "backgroundColor": "rgba(202, 201, 197, 0.5)",
                "borderColor": "rgba(202, 201, 197, 1)",
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
    heart_data = BloodPressure.objects.filter(DEVICE=devices)
    i = 0
    for ht in heart_data:
        blood_pressure_labels.append(str(ht.DATETIME.time()))
        blood_pressure_data.append(ht.VALUE)
        i += 1
        if i > 9:
            break

    blood_pressure = {
        "labels": blood_pressure_labels,
        "datasets": [
            {
                "data": blood_pressure_data,
                "backgroundColor": "rgba(202, 201, 197, 0.5)",
                "borderColor": "rgba(202, 201, 197, 1)",
                "pointBackgroundColor": "rgba(35, 78, 123, 0.69)",
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
