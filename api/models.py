from django.contrib.auth.models import AbstractUser
from django.db import models
from shortuuid import uuid
from django.core.validators import EmailValidator, FileExtensionValidator

# Create your models here.
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True, validators=[EmailValidator])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]

    def save(self, *args, **kwargs):
        user_email = self.email.split("@")[0]

        if not self.username:
            self.username = f"{user_email}_{uuid()[:4]}_{uuid()[:4]}"

        if not self.full_name:
            self.full_name = self.username

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.email})"


class Profile(TimestampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile_pics/", default="profile_pics/default.png",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])
        ]
    )
    city = models.CharField(max_length=60, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return getattr(self.user, "username", "Profile")
