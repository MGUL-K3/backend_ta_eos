from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)

    name = models.CharField(_("first name"), max_length=70)
    surname = models.CharField(_("last name"), max_length=70)
    patronymic = models.CharField(_("patronymic"), max_length=70)
    group = models.CharField(_("university group"), max_length=70)

    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    is_active = models.BooleanField(_("active"), default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    last_visit = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname", "patronymic", "group"]

    objects = UserManager()

    class Meta:
        verbose_name = _("users")
        verbose_name_plural = _("users")

    def get_full_name(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    def get_short_name(self):
        return "{} {}".format(self.surname, self.group)

    def update_last_visit(self):
        self.last_visit = timezone.now()
        self.save()
