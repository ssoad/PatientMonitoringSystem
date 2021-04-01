from django.contrib import admin
from django.urls import path

from Accounts.views import login_view
from DeviceController.views import deviceList
from GraphController.views import line_chart, line_chart_json, dataView
from DataController.views import HeartRateData, BloodPressureData, saveData, index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices', deviceList),
    path('login', login_view),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('heart_data/<str:ip>', HeartRateData),
    path('blood_data/<str:ip>', BloodPressureData),
    path('view/<str:ip>', dataView),
    path('saveData', saveData),
    path('get', index)

]
