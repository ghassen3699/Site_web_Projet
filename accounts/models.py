from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _









class CustomUserManager(BaseUserManager) :

    def _create_user(self, email , password = None, **extra_fields) :

        if not email :
            raise ValueError('Votre Adresse mail est déja utiliser')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email , password=None, **extra_fields) :
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password = None, **extra_fields) :
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True :
            raise ValueError('Superuser a is_staff = True')
        if extra_fields.get('is_superuser') is not True :
            raise ValueError('Superuser a is_super_user = True')
        
        return self._create_user(email, password, **extra_fields)










class CustomUser(AbstractUser) :
    username = None
    email = models.EmailField(_('email'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()