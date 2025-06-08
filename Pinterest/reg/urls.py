from django.urls import path
from .views import (
    home, register_view, mainpage, CustomLoginView, logout_view, callback_view,
    userprofile, create_pin, pin_detail
)

# === Principle: DRY (немає дублювання шляхів), KISS (чітка структура) ===

urlpatterns = [
    path('', home, name='home'),  # Головна (лендинг)
    path('mainpage/', mainpage, name='mainpage'),  # Сторінка з пінами/пошуком
    path('register/', register_view, name='register'),  # Реєстрація
    path('login/', CustomLoginView.as_view(), name='login'),  # Логін
    path('logout/', logout_view, name='logout'),  # Вихід

    path(
        'accounts/google/login/callback/',
        callback_view,    # Google-логін callback
        name='google_callback'
    ),
    path('userprofile/', userprofile, name='userprofile'),  # Мій профіль
    path('create_pin/', create_pin, name='create_pin'),  # Створення піну
    path('pin/<int:pin_id>/', pin_detail, name='pin_detail'),  # Детальна сторінка піну
]
