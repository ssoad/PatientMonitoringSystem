from django.contrib import admin
from django.urls import path

from Accounts.views import login_view, dashboard, logout_view, home
from DeviceController.views import deviceList, deviceView
from GraphController.views import line_chart, line_chart_json, dataView
from DataController.views import HeartRateData, BloodPressureData, saveData, index, TemperatureData, HumidityData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices', deviceList),
    path('login', login_view, name='login'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('heart_data/<str:ip>', HeartRateData),
    path('blood_data/<str:ip>', BloodPressureData),
    path('temp_data/<str:ip>', TemperatureData),
    path('humidity_data/<str:ip>', HumidityData),
    path('view/<str:ip>', dataView),
    path('saveData', saveData),
    path('get', index),
    path('dashboard', dashboard,name='dashboard'),
    path('devicelist', deviceView, name='devices'),
    path('logout', logout_view, name='logout'),
    path('', home)

]
