from django.contrib import admin
from django.urls import path

from GraphController.views import line_chart, line_chart_json, dataView
from DataController.views import HeartRateData, BloodPressureData, saveData
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('heart_data/<str:ip>', HeartRateData),
    path('blood_data/<str:ip>', BloodPressureData),
    path('view/<str:ip>', dataView),
    path('saveData', saveData)
]
