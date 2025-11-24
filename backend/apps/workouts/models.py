from django.db import models
from ..users.models import User
import uuid
from django.conf import settings

class Workout(models.Model):

    STATUS_CHOICE = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout')

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='planned')
    is_public = models.BooleanField(default=False)

    duration = models.PositiveIntegerField(null=True, blank=True, help_text='Duration in minutes')
    date = models.DateField()
    notes = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username} - {self.date}"

class Exercise(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)


    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    target_muscle = models.CharField(max_length=50)
    muscles_secondary = models.TextField(blank=True) 
    
    equipment = models.CharField(max_length=50, blank=True)
    difficulty = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    
    category = models.CharField(max_length=50)
    is_compound = models.BooleanField(default=False)

    sets = models.IntegerField(default=0)
    reps = models.CharField(max_length=50, blank=True)
    weight = models.FloatField(default=0)
    
    duration = models.IntegerField(default=0)  # seconds
    distance = models.FloatField(default=0)    # meters
    rest_time = models.IntegerField(default=0) # seconds
    
    video_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="exercises/", blank=True)
    
    instructions = models.TextField(blank=True)
    tips = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.workout.title}"
