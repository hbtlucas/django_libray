from django.db import models

class Usuario(models.Model):
    user = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    password = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.user