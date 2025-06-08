from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class UserManager(BaseUserManager):
    """
    Factory Method pattern: менеджер для створення звичайних та суперкористувачів.
    """
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Створює та повертає користувача з заданими username, email та паролем.
        """
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email) if email else None
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Створює та повертає суперкористувача з усіма правами.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Кастомна модель користувача, розширює AbstractBaseUser.
    """
    username = models.CharField(max_length=20, unique=True, verbose_name="Нікнейм")
    name = models.CharField(max_length=30, blank=True, verbose_name="Ім'я")
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="Email")
    desc = models.TextField(max_length=100, blank=True, verbose_name="Опис")

    pfp = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        verbose_name="Аватар"
    )

    is_active = models.BooleanField(default=True, verbose_name="Активний")
    is_staff = models.BooleanField(default=False, verbose_name="Адміністратор")

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        verbose_name="Групи"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        verbose_name="Права"
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class Pin(models.Model):
    """
    Модель піну (інспірації/поста користувача).
    """
    title = models.CharField(
        max_length=40,
        verbose_name="Назва"
    )
    desc = models.TextField(
        max_length=100,
        blank=True,
        verbose_name="Опис"
    )
    pic = models.ImageField(
        upload_to='pin_pics/',
        blank=True, null=True,
        verbose_name="Зображення"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name="Користувач"
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-id']
        verbose_name = "Пін"
        verbose_name_plural = "Піни"


class Board(models.Model):
    """
    Модель дошки, яка обʼєднує піни.
    """
    name = models.CharField(
        max_length=255,
        verbose_name="Назва дошки"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Власник"
    )
    pins = models.ManyToManyField(Pin, verbose_name="Піни")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Дошка"
        verbose_name_plural = "Дошки"
        ordering = ['-id']
