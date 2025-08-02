import os 
import django

# встановлюємо віртуальну змінну, де вказуємо де знаходиться наш файл settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstproject.settings")
django.setup()

from accounts.models import Role, User

# створимо кілька ролей
# Role.objects.create(title = "admin")
# Role.objects.create(title = "user")

# Створюємо нових юзерів
admin_role = Role.objects.get(title="admin")
user_role = Role.objects.get(title="user")

User.objects.create(name="TestUser", email="testUser@gmail.com", role=admin_role)
User.objects.create(name="TestUser2", email="testUser2@gmail.com", role=user_role)