from django.test import TestCase  # Импортируем класс TestCase для создания тестов
from rest_framework.test import APIRequestFactory  # Импортируем APIRequestFactory для создания тестовых запросов
from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from django.contrib.auth.models import AnonymousUser  # Импортируем класс AnonymousUser для представления анонимного пользователя
from patients.permissions import IsDoctorPermission  # Импортируем класс IsDoctorPermission для проверки прав доступа

User = get_user_model()  # Получаем модель пользователя

class IsDoctorPermissionTest(TestCase):  # Класс для тестирования прав доступа для врачей
    def setUp(self):  # Метод, который выполняется перед каждым тестом
        self.permission = IsDoctorPermission()  # Инициализируем объект разрешения
        self.factory = APIRequestFactory()  # Создаем экземпляр APIRequestFactory для создания запросов
        
        # Создаем пользователей с разными ролями
        self.doctor = User.objects.create_user(  # Создаем пользователя с ролью 'doctor'
            username='doctor',
            password='doctor123',
            role='doctor'
        )
        self.patient = User.objects.create_user(  # Создаем пользователя с ролью 'patient'
            username='patient',
            password='patient123',
            role='patient'
        )
        self.anonymous_user = AnonymousUser()  # Создаем анонимного пользователя

    def test_doctor_has_permission(self):  # Тест для проверки, что врач имеет разрешение
        request = self.factory.get('/')  # Создаем GET-запрос
        request.user = self.doctor  # Устанавливаем пользователя как врача
        self.assertTrue(self.permission.has_permission(request, None))  # Проверяем, что разрешение предоставлено

    def test_patient_has_no_permission(self):  # Тест для проверки, что пациент не имеет разрешения
        request = self.factory.get('/')  # Создаем GET-запрос
        request.user = self.patient  # Устанавливаем пользователя как пациента
        self.assertFalse(self.permission.has_permission(request, None))  # Проверяем, что разрешение не предоставлено

    def test_anonymous_user_has_no_permission(self):  # Тест для проверки, что анонимный пользователь не имеет разрешения
        request = self.factory.get('/')  # Создаем GET-запрос
        request.user = self.anonymous_user  # Устанавливаем пользователя как анонимного
        self.assertFalse(self.permission.has_permission(request, None))  # Проверяем, что разрешение не предоставлено

    def test_none_user_has_no_permission(self):  # Тест для проверки, что пользователь None не имеет разрешения
        request = self.factory.get('/')  # Создаем GET-запрос
        request.user = None  # Устанавливаем пользователя как None
        self.assertFalse(self.permission.has_permission(request, None))  # Проверяем, что разрешение не предоставлено