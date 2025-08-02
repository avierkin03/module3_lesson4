from django.db import models

# Модель "Роль"
class Role(models.Model):
    title = models.CharField(max_length=20, unique=True)


# Модель "Користувач"
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null = True)