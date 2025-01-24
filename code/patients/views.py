from rest_framework import generics  # Импортируем базовые классы представлений из Django REST Framework
from rest_framework.permissions import IsAuthenticated  # Импортируем разрешение для проверки аутентификации пользователя
from .models import Patient  # Импортируем модель Patient из текущего приложения
from .serializers import PatientSerializer  # Импортируем сериализатор PatientSerializer
from .permissions import IsDoctorPermission  # Импортируем пользовательское разрешение IsDoctorPermission


class PatientListView(generics.ListAPIView):  # Создаем представление для отображения списка пациентов
    queryset = Patient.objects.all()  # Определяем набор данных - все объекты Patient
    serializer_class = PatientSerializer  # Указываем сериализатор, который будет использоваться для преобразования данных
    permission_classes = [IsAuthenticated, IsDoctorPermission]  # Устанавливаем классы разрешений: пользователь должен быть аутентифицирован и иметь роль врача