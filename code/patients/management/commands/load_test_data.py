from django.core.management.base import BaseCommand  # Импортируем базовый класс команды
from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from patients.models import Patient  # Импортируем модель пациента
from datetime import date  # Импортируем класс date для работы с датами

User = get_user_model()  # Получаем модель пользователя

class Command(BaseCommand):
    help = 'Loads test data into the database'  # Описание команды

    def handle(self, *args, **kwargs):
        # Создание пользователей
        users_data = [
            {
                'username': 'admin',
                'email': 'admin@example.com',
                'password': 'admin123',
                'role': 'doctor',
                'first_name': 'Admin',
                'last_name': 'Super',
                'is_staff': True,
                'is_superuser': True,
            },
            {
                'username': 'doctor',
                'email': 'doctor@example.com',
                'password': 'doctor123',
                'role': 'doctor',
                'first_name': 'John',
                'last_name': 'Doe',
                'is_staff': True,
            },
            {
                'username': 'patient',
                'email': 'patient@example.com',
                'password': 'patient123',
                'role': 'patient',
                'first_name': 'Jane',
                'last_name': 'Smith',
            }
        ]

        # Проходим по каждому набору данных пользователя
        for user_data in users_data:
            # Проверяем, существует ли пользователь с таким именем
            if not User.objects.filter(username=user_data['username']).exists():
                # Если это суперпользователь, создаем его
                if user_data.get('is_superuser'):
                    user = User.objects.create_superuser(
                        username=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password'],
                        role=user_data['role']
                    )
                else:
                    # В противном случае создаем обычного пользователя
                    user = User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password'],
                        role=user_data['role'],
                        is_staff=user_data.get('is_staff', False)
                    )
                
                # Устанавливаем имя и фамилию пользователя
                user.first_name = user_data.get('first_name', '')
                user.last_name = user_data.get('last_name', '')
                user.save()
                
                # Выводим сообщение об успешном создании пользователя
                self.stdout.write(
                    self.style.SUCCESS(f"User {user_data['username']} created successfully")
                )

        # Создание тестовых пациентов
        test_patients = [
            {
                'date_of_birth': date(1990, 5, 15),
                'diagnoses': ['Грипп', 'ОРВИ']
            },
            {
                'date_of_birth': date(1985, 3, 20),
                'diagnoses': ['Гипертония', 'Диабет']
            },
            {
                'date_of_birth': date(1995, 8, 10),
                'diagnoses': ['Бронхит']
            },
            {
                'date_of_birth': date(1978, 12, 25),
                'diagnoses': ['Артрит', 'Остеохондроз']
            }
        ]

        # Проверяем, существуют ли уже пациенты
        if not Patient.objects.exists():
            # Проходим по данным тестовых пациентов
            for patient_data in test_patients:
                # Создаем нового пациента с предоставленными данными
                Patient.objects.create(**patient_data)
            # Выводим сообщение об успешном создании тестовых пациентов
            self.stdout.write(self.style.SUCCESS('Тестовые пациенты успешно созданы')) 