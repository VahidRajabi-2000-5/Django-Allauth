from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    