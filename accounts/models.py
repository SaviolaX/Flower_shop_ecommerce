from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    
    def __str__(self) -> str:
        return self.email
