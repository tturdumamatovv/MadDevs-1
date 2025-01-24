from django.db import models  # Импортируем базовый класс моделей Django
from django.contrib.postgres.fields import ArrayField  # Импортируем ArrayField для хранения массивов
from django.contrib.auth.models import AbstractUser  # Импортируем класс AbstractUser для создания пользовательской модели


class User(AbstractUser):  # Создаем модель User, наследующую от AbstractUser
    ROLES = (  # Определяем кортеж с ролями пользователей
        ('doctor', 'Doctor'),  # Роль врача
        ('patient', 'Patient'),  # Роль пациента
    )
    
    role = models.CharField(  # Поле для хранения роли пользователя
        max_length=10,  # Максимальная длина строки
        choices=ROLES,  # Доступные варианты ролей
        default='patient'  # Значение по умолчанию
    )

    class Meta:  # Метаданные для модели User
        verbose_name = "Пользователь"  # Человекочитаемое имя модели
        verbose_name_plural = "Пользователи"  # Человекочитаемое имя модели во множественном числе
        ordering = ['-id']  # Порядок сортировки по убыванию ID


class Patient(models.Model):  # Создаем модель Patient
    date_of_birth = models.DateField(  # Поле для хранения даты рождения пациента
        verbose_name="Дата рождения"  # Человекочитаемое имя поля
    )
    diagnoses = ArrayField(  # Поле для хранения массива диагнозов
        models.CharField(max_length=255),  # Элементы массива - строки с максимальной длиной 255
        verbose_name="Диагнозы"  # Человекочитаемое имя поля
    )
    created_at = models.DateTimeField(  # Поле для хранения даты и времени создания записи
        auto_now_add=True,  # Автоматически устанавливается при создании
        verbose_name="Дата создания записи"  # Человекочитаемое имя поля
    )
    updated_at = models.DateTimeField(  # Поле для хранения даты и времени последнего обновления записи
        auto_now=True,  # Автоматически обновляется при изменении
        verbose_name="Дата обновления записи"  # Человекочитаемое имя поля
    )

    class Meta:  # Метаданные для модели Patient
        verbose_name = "Пациент"  # Человекочитаемое имя модели
        verbose_name_plural = "Пациенты"  # Человекочитаемое имя модели во множественном числе
        ordering = ['-created_at']  # Порядок сортировки по убыванию даты создания

    def __str__(self):  # Метод для строкового представления объекта Patient
        return f"Пациент {self.id} ({self.date_of_birth})"  # Возвращаем строку с ID и датой рождения пациента