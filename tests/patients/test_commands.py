from io import StringIO  # Импортируем StringIO для захвата вывода команды
from django.core.management import call_command  # Импортируем функцию для вызова команд управления Django
from django.test import TestCase  # Импортируем класс TestCase для создания тестов
from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from patients.models import Patient  # Импортируем модель Patient из приложения patients

User = get_user_model()  # Получаем модель пользователя

class LoadTestDataCommandTest(TestCase):  # Создаем класс тестов для команды загрузки тестовых данных
    def test_command_output(self):  # Метод для тестирования вывода команды
        out = StringIO()  # Создаем объект StringIO для захвата вывода
        call_command('load_test_data', stdout=out)  # Вызываем команду загрузки тестовых данных
        
        # Проверяем, что пользователи созданы
        self.assertTrue(User.objects.filter(username='admin').exists())  # Проверяем наличие пользователя 'admin'
        self.assertTrue(User.objects.filter(username='doctor').exists())  # Проверяем наличие пользователя 'doctor'
        self.assertTrue(User.objects.filter(username='patient').exists())  # Проверяем наличие пользователя 'patient'
        
        # Проверяем роли и права пользователей
        admin = User.objects.get(username='admin')  # Получаем суперпользователя 'admin'
        self.assertTrue(admin.is_superuser)  # Проверяем, что 'admin' является суперпользователем
        self.assertTrue(admin.is_staff)  # Проверяем, что 'admin' является сотрудником
        self.assertEqual(admin.role, 'doctor')  # Проверяем роль 'admin'
        self.assertEqual(admin.first_name, 'Admin')  # Проверяем имя 'admin'
        self.assertEqual(admin.last_name, 'Super')  # Проверяем фамилию 'admin'
        
        doctor = User.objects.get(username='doctor')  # Получаем пользователя 'doctor'
        self.assertFalse(doctor.is_superuser)  # Проверяем, что 'doctor' не является суперпользователем
        self.assertTrue(doctor.is_staff)  # Проверяем, что 'doctor' является сотрудником
        self.assertEqual(doctor.role, 'doctor')  # Проверяем роль 'doctor'
        self.assertEqual(doctor.first_name, 'John')  # Проверяем имя 'doctor'
        self.assertEqual(doctor.last_name, 'Doe')  # Проверяем фамилию 'doctor'
        
        patient = User.objects.get(username='patient')  # Получаем пользователя 'patient'
        self.assertFalse(patient.is_superuser)  # Проверяем, что 'patient' не является суперпользователем
        self.assertFalse(patient.is_staff)  # Проверяем, что 'patient' не является сотрудником
        self.assertEqual(patient.role, 'patient')  # Проверяем роль 'patient'
        self.assertEqual(patient.first_name, 'Jane')  # Проверяем имя 'patient'
        self.assertEqual(patient.last_name, 'Smith')  # Проверяем фамилию 'patient'
        
        # Проверяем, что пациенты созданы
        self.assertEqual(Patient.objects.count(), 4)  # Проверяем количество созданных пациентов
        
        # Проверяем данные одного из пациентов
        patient = Patient.objects.first()  # Получаем первого пациента
        self.assertIsNotNone(patient.date_of_birth)  # Проверяем, что дата рождения не None
        self.assertTrue(isinstance(patient.diagnoses, list))  # Проверяем, что диагнозы представлены в виде списка