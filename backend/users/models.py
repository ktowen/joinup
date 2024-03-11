from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from services.email.handler import EmailService
from services.sms.handler import SMSService


class UserManager(BaseUserManager):
    """
    Based on the default UserManager, but with the create_user and create_superuser methods overridden
    to use the email field instead of the username field.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_email_verified = models.BooleanField(_("email verified"), default=False)

    phone = PhoneNumberField(_("phone number"))
    is_phone_verified = models.BooleanField(_("phone number verified"), default=False)

    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    hobbies = models.TextField(_("hobbies"), blank=True)

    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def send_verification_sms(self):
        sms_service = SMSService()
        sms_service.send(self.phone, "Click here to verify your phone number.")

    def send_verification_email(self):
        email_service = EmailService()
        email_service.send(self.email, "Click here to verify your email.")
