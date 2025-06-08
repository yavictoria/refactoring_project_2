from django.apps import AppConfig

class RegConfig(AppConfig):
    """
    Стандартна Django AppConfig.
    Principle: Single Responsibility — відповідає лише за конфігурацію додатку reg.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg'
