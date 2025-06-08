from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Pin, Board
from .forms import CustomUserCreationForm, CustomUserChangeForm

# === Principle: Open/Closed (легко розширити через кастомну адмінку), DRY, KISS ===

class CustomUserAdmin(BaseUserAdmin):
    """
    Кастомна адмінка для моделі User.
    Патерн: Adapter (адаптує стандартний UserAdmin під нашу модель).
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('email', 'username', 'name', 'is_staff', 'is_active')
    list_filter = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'name', 'desc', 'password', 'pfp')
        }),
        ('Права', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'name',
                'password1', 'password2',
                'is_staff',
                'is_active'),
        }),
    )

# === Додаємо Pin і Board у адмінку з мінімальними налаштуваннями ===

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    """
    Адмінка для Pin.
    Principle: Single Responsibility.
    """
    list_display = ('title', 'user')
    search_fields = ('title', 'desc')
    list_filter = ('user',)

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """
    Адмінка для Board.
    """
    list_display = ('name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)

# === Реєстрація користувача з кастомною адмінкою ===
admin.site.register(User, CustomUserAdmin)
