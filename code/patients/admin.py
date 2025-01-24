from django.contrib import admin  # Импортируем модуль администрирования Django
from django.contrib.auth.admin import UserAdmin  # Импортируем класс UserAdmin для управления пользователями
from .models import User, Patient  # Импортируем модели User и Patient из текущего приложения


@admin.register(User)  # Регистрируем модель User в админке
class CustomUserAdmin(UserAdmin):  # Создаем класс для настройки отображения пользователей
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  # Поля, отображаемые в списке пользователей
    list_filter = ('role', 'is_staff', 'is_active')  # Фильтры для списка пользователей
    fieldsets = (  # Настройка полей на странице редактирования пользователя
        (None, {'fields': ('username', 'password')}),  # Основные поля
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),  # Личная информация
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Права доступа
        ('Important dates', {'fields': ('last_login', 'date_joined')}),  # Важные даты
    )
    add_fieldsets = (  # Поля для добавления нового пользователя
        (None, {
            'classes': ('wide',),  # Широкий класс для полей
            'fields': ('username', 'email', 'role', 'password1', 'password2'),  # Поля для добавления
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Поля для поиска пользователей
    ordering = ('username',)  # Порядок сортировки пользователей

    class Meta:  # Метаданные для админки
        verbose_name = "Пользователь"  # Человекочитаемое имя модели
        verbose_name_plural = "Пользователи"  # Человекочитаемое имя модели во множественном числе


@admin.register(Patient)  # Регистрируем модель Patient в админке
class PatientAdmin(admin.ModelAdmin):  # Создаем класс для настройки отображения пациентов
    list_display = ('id', 'date_of_birth', 'get_diagnoses', 'created_at')  # Поля, отображаемые в списке пациентов
    list_filter = ('created_at', 'date_of_birth')  # Фильтры для списка пациентов
    search_fields = ('diagnoses',)  # Поля для поиска пациентов
    ordering = ('-created_at',)  # Порядок сортировки пациентов по дате создания

    class Meta:  # Метаданные для админки
        verbose_name = "Пациент"  # Человекочитаемое имя модели
        verbose_name_plural = "Пациенты"  # Человекочитаемое имя модели во множественном числе

    def get_diagnoses(self, obj):  # Метод для получения диагнозов пациента
        return ", ".join(obj.diagnoses)  # Возвращаем диагнозы в виде строки
    get_diagnoses.short_description = 'Диагнозы'  # Человекочитаемое имя для столбца диагнозов