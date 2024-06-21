from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="images/")

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"
