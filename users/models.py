from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, tipo, password):
        user = self.model(
            username=username,
            tipo=tipo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, tipo, password):
        user = self.create_user(
            password=password,
            username=username,
            tipo=tipo,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, tipo, password):
        user = self.create_user(
            password=password,
            username=username,
            tipo=tipo
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    tipo = models.CharField(max_length=100)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'tipo' ]

    def __str__(self):              # __unicode__ on Python 2
        return self.username