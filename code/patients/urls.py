from django.urls import path  # Импортируем функцию path для определения маршрутов URL
from .views import PatientListView  # Импортируем представление PatientListView из views

app_name = 'patients'  # Устанавливаем пространство имен для приложения patients

urlpatterns = [  # Список маршрутов URL для приложения
    path('', PatientListView.as_view(), name='patient-list'),  # Определяем маршрут для списка пациентов
] 