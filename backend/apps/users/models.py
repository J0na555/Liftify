from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid


class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    GOAL_CHOICES = [
        ('weight loss', 'Weight Loss'),
        ('build muscle', 'Build Muscle')
    ]

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    full_name = models.CharField(max_length=225, blank=True)
    profile_image = models.URLField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='available')
    birth_date = models.DateField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    goal = models.CharField(max_length=30, choices=GOAL_CHOICES, default='available')
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.full_name if self.full_name else self.username
    
    @property
    def display_name(self):
        return self.full_name or self.username


