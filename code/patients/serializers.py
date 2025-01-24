from rest_framework import serializers  # Импортируем сериализаторы из Django REST Framework
from .models import Patient  # Импортируем модель Patient из текущего приложения


class PatientSerializer(serializers.ModelSerializer):  # Создаем сериализатор для модели Patient
    class Meta:
        model = Patient  # Указываем модель, для которой создается сериализатор
        fields = ['id', 'date_of_birth', 'diagnoses', 'created_at']  # Указываем поля, которые будут сериализованы