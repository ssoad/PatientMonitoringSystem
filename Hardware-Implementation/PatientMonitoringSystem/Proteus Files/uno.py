
import requests
import json
webpage = "http://10.0.167.21"
device_ip= '10.0.0.2'

while True:
    request = requests.get(webpage)
    r = (request.json())
    data1 = {
            "ip_address" : device_ip,
            "heart_rate" : r['heart_rate'],
            "blood_pressure" : r['bmp'],
            "temperature" : r['temp'],
            "humidity" : r['humidity']
    }
    url = 'http://http://ssoad.pythonanywhere.com/saveData'
    r = requests.post(url, data1)
    if r.status_code == 200:
        print("OK")