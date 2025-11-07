from django.db import models
from ..users.models import User
import uuid
from django.conf import settings

class Workout(models.Model):

    STATUS_CHOICE = [
        ('planned', 'Planned'),
        ('completed', 'Completed')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout')
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='planned')
    duration = models.PositiveIntegerField(null=True, blank=True, help_text='Duration in minutes')
    is_public = models.BooleanField(default=False)
    date = models.DateField()
    notes = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)