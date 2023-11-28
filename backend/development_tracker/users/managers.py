"""Defining a manager for models of 'Users' application."""

from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    """Modified user manager.

    Creates and saves a users by email.
    """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email address must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
