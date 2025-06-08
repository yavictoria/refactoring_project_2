# reg/adapters.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

# === Патерн Adapter ===
# Клас адаптує сторонню бібліотеку allauth до логіки твого додатку (структурний патерн Adapter).

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Adapter Pattern: дозволяє інтегрувати логіку редіректу після соц-логіну у власний workflow.
    """
    def get_login_redirect_url(self, request):
        """
        Перенаправлення користувача після успішного соц-логіну (Google).
        """
        return '/mainpage/'
