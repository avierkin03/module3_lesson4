import os 
import django

#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstproject.settings")
django.setup()

from accounts.models import Role, User

# створимо кілька ролей
# Role.objects.create(title = "user")

# Role.objects.get(id = 2).delete()

admin_role = Role.objects.get(title="admin")

User.objects.create(name="TestUser", email="testUser@gmail.com", role=admin_role)