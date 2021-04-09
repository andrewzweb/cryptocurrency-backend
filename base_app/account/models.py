from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    picture = models.ImageField(blank=True)
    name = models.CharField(max_length=72, default='User', unique=True)

    def save(self, *args, **kwargs):
        self.name = self.user.username
        super(Account, self).save(*args, **kwargs)
