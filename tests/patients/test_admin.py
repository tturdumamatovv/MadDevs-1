from django.test import TestCase, Client  # Импортируем классы для тестирования
from django.urls import reverse  # Импортируем функцию для получения URL по имени
from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from patients.models import Patient  # Импортируем модель Patient из приложения patients
from datetime import date  # Импортируем класс date для работы с датами

User = get_user_model()  # Получаем модель пользователя

class AdminTest(TestCase):  # Создаем класс тестов для админки
    def setUp(self):  # Метод, который выполняется перед каждым тестом
        self.client = Client()  # Создаем экземпляр клиента для тестирования
        
        # Создаем суперпользователя с ролью 'doctor'
        self.admin_user = User.objects.create_superuser(
            username='admin',  # Имя пользователя
            email='admin@example.com',  # Электронная почта
            password='admin123',  # Пароль
            role='doctor'  # Роль пользователя
        )
        self.client.login(username='admin', password='admin123')  # Логинимся как суперпользователь
        
        # Создаем тестового пациента с датой рождения и диагнозом
        self.patient = Patient.objects.create(
            date_of_birth=date(1990, 1, 1),  # Указываем дату рождения
            diagnoses=['Тест']  # Указываем диагноз
        )

    def test_user_changelist(self):  # Тест для проверки списка пользователей в админке
        url = reverse('admin:patients_user_changelist')  # Получаем URL для списка пользователей
        response = self.client.get(url)  # Выполняем GET-запрос
        self.assertEqual(response.status_code, 200)  # Проверяем, что статус ответа 200

    def test_patient_changelist(self):  # Тест для проверки списка пациентов в админке
        url = reverse('admin:patients_patient_changelist')  # Получаем URL для списка пациентов
        response = self.client.get(url)  # Выполняем GET-запрос
        self.assertEqual(response.status_code, 200)  # Проверяем, что статус ответа 200

    def test_patient_change(self):  # Тест для проверки страницы изменения пациента
        url = reverse('admin:patients_patient_change', args=[self.patient.id])  # Получаем URL для изменения пациента
        response = self.client.get(url)  # Выполняем GET-запрос
        self.assertEqual(response.status_code, 200)  # Проверяем, что статус ответа 200

    def test_patient_add(self):  # Тест для проверки страницы добавления пациента
        url = reverse('admin:patients_patient_add')  # Получаем URL для добавления пациента
        response = self.client.get(url)  # Выполняем GET-запрос
        self.assertEqual(response.status_code, 200)  # Проверяем, что статус ответа 200

    def test_patient_delete(self):  # Тест для проверки страницы удаления пациента
        url = reverse('admin:patients_patient_delete', args=[self.patient.id])  # Получаем URL для удаления пациента
        response = self.client.get(url)  # Выполняем GET-запрос
        self.assertEqual(response.status_code, 200)  # Проверяем, что статус ответа 200