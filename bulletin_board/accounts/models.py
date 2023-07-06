import random

from django.contrib.auth.models import User
from django.db import models


class UserCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        code_num = (random.randint(10000, 99999))
        self.code = code_num
        super().save(*args, **kwargs)