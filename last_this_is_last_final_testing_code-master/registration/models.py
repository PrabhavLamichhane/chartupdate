# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save


# Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=300, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     email_confirmed = models.BooleanField(default=False)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()


# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyAccountManager(BaseUserManager):
    # Override to method

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not first_name:
            raise ValueError("Users must have an First name")
        if not last_name:
            raise ValueError("Users must have an Last name")

        user = self.model(
            email=self.normalize_email(email),  # email to lowercase
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=60, unique=True)
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30,)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# class Profile(models.Model):
#     user = models.OneToOneField(Account, on_delete=models.CASCADE)
#     # bio = models.TextField(max_length=500, blank=True)
#     # location = models.CharField(max_length=300, blank=True)
#     # birth_date = models.DateField(null=True, blank=True)
