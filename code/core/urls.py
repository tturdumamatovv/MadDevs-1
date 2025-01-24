"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Импортируем админку Django
from django.urls import path, include  # Импортируем функции для маршрутизации
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Импортируем представление для получения JWT токена
    TokenRefreshView,  # Импортируем представление для обновления JWT токена
)
from drf_spectacular.views import (
    SpectacularAPIView,  # Импортируем представление для генерации схемы API
    SpectacularSwaggerView,  # Импортируем представление для отображения документации Swagger
)

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для доступа к админке

    # JWT endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL для получения JWT токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # URL для обновления JWT токена

    # API endpoints
    path('patients/', include('patients.urls')),  # Включаем маршруты приложения patients

    # API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # URL для получения схемы API
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # URL для отображения документации Swagger
]
