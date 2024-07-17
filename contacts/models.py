import os

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.files import File
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Contact(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL
    )
    image = models.ImageField(blank=True, upload_to="images/")

    def get_full_name(self):
        return self.name if not self.surname else f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        if not self.image:
            default_image_path = os.path.join("images", "default.png")

            with open(os.path.join(settings.MEDIA_ROOT, default_image_path), "rb") as f:
                self.image.save("default.png", File(f), save=False)

        super().save(*args, **kwargs)
