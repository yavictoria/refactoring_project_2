from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import SignUpForm, CustomLoginForm, PinForm, EditProfileForm
from .models import Pin

# === Strategy Pattern: AUTHENTICATION_BACKENDS дозволяє підключати різні бекенди ===

def mainpage(request):
    """
    Головна сторінка з пошуком і відображенням пінів.
    Використовує DRY-принцип: логіка пошуку централізована.
    """
    query = request.GET.get('q', '')
    if query:
        pins = Pin.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    else:
        pins = Pin.objects.all().order_by('?')
    return render(request, 'mainpage.html', {'pins': pins, 'query': query})


def register_view(request):
    """
    View для реєстрації користувача.
    Використання Factory Method (SignUpForm).
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('mainpage')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# pylint: disable=too-many-ancestors
class CustomLoginView(LoginView):
    """
    LoginView з Template Method Pattern — кастомізуємо тільки потрібні методи.
    """
    form_class = CustomLoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        """
        Викликається при успішному логіні.
        """
        user = form.get_user()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return '/mainpage/'


def logout_view(request):
    """
    View для виходу користувача. Дотримання KISS/Single Responsibility.
    """
    logout(request)
    return redirect('home')


def home(request):
    """Гостьова сторінка (landing page)."""
    return render(request, "index.html")


def callback_view(request):
    """Callback після соц-логіну."""
    return redirect('mainpage')


@login_required
def userprofile(request):
    """
    Перегляд і редагування профілю користувача.
    Single Responsibility: логіка edit profile тільки тут.
    """
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'userprofile.html', {'form': form})


@login_required
def create_pin(request):
    """
    Створення нового піну для користувача.
    """
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            return redirect('userprofile')
    else:
        form = PinForm()
    return render(request, 'create_pin.html', {'form': form})


@login_required
def pin_detail(request, pin_id):
    """
    Перегляд детальної інформації про пін.
    """
    pin = get_object_or_404(Pin, id=pin_id)
    return render(request, 'pin_detail.html', {'pin': pin})
