from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# === Principle: Single Responsibility — головний роутер проекту лише делегує, нічого не дублює ===
# DRY: static() автоматично підхоплює налаштування з settings.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Адмінка Django
    path('accounts/', include('allauth.urls')),  # Усі соц-логіни (allauth)
    path('', include('reg.urls')),  # Головний функціонал проекту (реєстрація, піни тощо)
]

# Додаємо маршрути для медіа-файлів у режимі DEBUG (це best practice для student/demo-проекту)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
