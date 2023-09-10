from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6)  # Поле для хранения 6-значного кода

    def __str__(self):
        return self.user.username

