from rest_framework import permissions  # Импортируем базовый класс разрешений из Django REST Framework


class IsDoctorPermission(permissions.BasePermission):  # Создаем класс разрешений для проверки роли врача
    def has_permission(self, request, view):  # Метод для проверки разрешений
        # Проверяем, что пользователь аутентифицирован и имеет роль doctor
        return bool(request.user and request.user.is_authenticated and request.user.role == 'doctor')  # Возвращаем True, если пользователь аутентифицирован и его роль - doctor