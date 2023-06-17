from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email is required.')

        if not name:
            raise ValueError('Name is required.')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError('Email is required.')

        if not name:
            raise ValueError('Name is required.')

        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email',
                              unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class File(models.Model):
    FILE_STATUS_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    )

    file_name = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_files/')
    file_status = models.CharField(max_length=10, choices=FILE_STATUS_CHOICES)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name='uploaded_files'
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    allowed_emails = models.ManyToManyField(
        CustomUser, blank=True, related_name='allowed_files')

    def __str__(self):
        return self.file_name

    def get_delete_url(self):
        return reverse('delete_file', args=[self.pk])
