from django.test import TestCase  # Импортируем класс TestCase для создания тестов
from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from patients.models import Patient  # Импортируем модель Patient из приложения patients
from datetime import date  # Импортируем класс date для работы с датами

User = get_user_model()  # Получаем модель пользователя

class UserModelTest(TestCase):  # Класс для тестирования модели пользователя
    def setUp(self):  # Метод, который выполняется перед каждым тестом
        self.user_data = {  # Данные для создания тестового пользователя
            'username': 'testuser',  # Имя пользователя
            'email': 'test@example.com',  # Электронная почта
            'password': 'testpass123',  # Пароль
            'role': 'doctor',  # Роль пользователя
            'first_name': 'Test',  # Имя
            'last_name': 'User'  # Фамилия
        }
        self.user = User.objects.create_user(**self.user_data)  # Создаем тестового пользователя

    def test_user_creation(self):  # Тест для проверки создания пользователя
        self.assertTrue(isinstance(self.user, User))  # Проверяем, что созданный объект является пользователем
        self.assertEqual(self.user.username, self.user_data['username'])  # Проверяем имя пользователя
        self.assertEqual(self.user.email, self.user_data['email'])  # Проверяем электронную почту
        self.assertEqual(self.user.role, self.user_data['role'])  # Проверяем роль пользователя
        self.assertEqual(self.user.first_name, self.user_data['first_name'])  # Проверяем имя
        self.assertEqual(self.user.last_name, self.user_data['last_name'])  # Проверяем фамилию

    def test_user_str_representation(self):  # Тест для проверки строкового представления пользователя
        self.assertEqual(str(self.user), self.user_data['username'])  # Проверяем строковое представление

    def test_user_default_role(self):  # Тест для проверки роли по умолчанию
        user = User.objects.create_user(username='defaultuser', password='pass123')  # Создаем пользователя без роли
        self.assertEqual(user.role, 'patient')  # Проверяем, что роль по умолчанию - 'patient'

    def test_user_meta_options(self):  # Тест для проверки мета-опций модели пользователя
        self.assertEqual(User._meta.verbose_name, 'Пользователь')  # Проверяем отображаемое имя
        self.assertEqual(User._meta.verbose_name_plural, 'Пользователи')  # Проверяем отображаемое имя во множественном числе
        self.assertEqual(User._meta.ordering, ['-id'])  # Проверяем порядок сортировки

class PatientModelTest(TestCase):  # Класс для тестирования модели пациента
    def setUp(self):  # Метод, который выполняется перед каждым тестом
        self.patient_data = {  # Данные для создания тестового пациента
            'date_of_birth': date(1990, 1, 1),  # Дата рождения
            'diagnoses': ['Грипп', 'ОРВИ']  # Диагнозы
        }
        self.patient = Patient.objects.create(**self.patient_data)  # Создаем тестового пациента

    def test_patient_creation(self):  # Тест для проверки создания пациента
        self.assertTrue(isinstance(self.patient, Patient))  # Проверяем, что созданный объект является пациентом
        self.assertEqual(self.patient.date_of_birth, self.patient_data['date_of_birth'])  # Проверяем дату рождения
        self.assertEqual(self.patient.diagnoses, self.patient_data['diagnoses'])  # Проверяем диагнозы
        self.assertIsNotNone(self.patient.created_at)  # Проверяем, что дата создания не None
        self.assertIsNotNone(self.patient.updated_at)  # Проверяем, что дата обновления не None

    def test_patient_str_representation(self):  # Тест для проверки строкового представления пациента
        expected = f"Пациент {self.patient.id} ({self.patient.date_of_birth})"  # Ожидаемое строковое представление
        self.assertEqual(str(self.patient), expected)  # Проверяем строковое представление

    def test_patient_ordering(self):  # Тест для проверки порядка сортировки пациентов
        patient2 = Patient.objects.create(  # Создаем второго пациента
            date_of_birth=date(1995, 1, 1),  # Дата рождения
            diagnoses=['Бронхит']  # Диагноз
        )
        patients = Patient.objects.all()  # Получаем всех пациентов
        self.assertEqual(patients[0], patient2)  # Проверяем, что новый пациент первый (ordering = ['-created_at'])

    def test_patient_meta_options(self):  # Тест для проверки мета-опций модели пациента
        self.assertEqual(Patient._meta.verbose_name, 'Пациент')  # Проверяем отображаемое имя
        self.assertEqual(Patient._meta.verbose_name_plural, 'Пациенты')  # Проверяем отображаемое имя во множественном числе
        self.assertEqual(Patient._meta.ordering, ['-created_at'])  # Проверяем порядок сортировки

    def test_patient_update(self):  # Тест для проверки обновления данных пациента
        new_diagnoses = ['Бронхит', 'Пневмония']  # Новые диагнозы
        old_updated_at = self.patient.updated_at  # Сохраняем старую дату обновления
        
        self.patient.diagnoses = new_diagnoses  # Обновляем диагнозы
        self.patient.save()  # Сохраняем изменения
        
        updated_patient = Patient.objects.get(id=self.patient.id)  # Получаем обновленного пациента
        self.assertEqual(updated_patient.diagnoses, new_diagnoses)  # Проверяем обновленные диагнозы
        self.assertGreater(updated_patient.updated_at, old_updated_at)  # Проверяем, что дата обновления изменилась