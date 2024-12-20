from django.db import models
from django.contrib.auth.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..settings.models import *


# class Base(models.Model):
#     id = models.AutoField(primary_key=True)
#     state = models.BooleanField(default=True)
#     create_to = models.DateTimeField(auto_now_add=True)
#     update_to = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True


class UserManagerModel(BaseUserManager):

    def _create_user(self, email, username, first_name, last_name, password, is_active, superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            superuser=superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        return self._create_user(email, username, first_name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):
        return self._create_user(email, username, first_name, last_name, password, True, True, **extra_fields)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rut_dgi = models.CharField(max_length=100)
    address = models.CharField(max_length=225, blank=True, null=True)
    address2 = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/company/', max_length=200, blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class UserModel(AbstractBaseUser):
    CUSTOMER = '1'
    EMPLOYEE = '2'
    USER_TYPE = (
        (CUSTOMER, 'CUSTOMER'),
        (EMPLOYEE, 'EMPLOYEE'),
    )

    username = models.CharField('Username', unique=True, max_length=100)
    first_name = models.CharField('First name', max_length=200, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=200, blank=True, null=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    superuser = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/users/', blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    objects = UserManagerModel()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.last_name},{self.first_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.superuser

    @property
    def is_activated(self):
        return self.is_active

    def natural_key(self):
        return f'{self.first_name} {self.last_name}'

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserModel.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name
