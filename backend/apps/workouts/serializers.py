from rest_framework import serializers
from .models import Workout, Exercise

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model= Workout
        fields = ['id','user', 'title', 'status', 'duration', 'is_public', 'date', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'target_muscle', 'muscles_secondary', 'equipment', 'difficulty', 'category', 'is_compound', 'sets', 'reps', 'weight', 'duration', 'distance, rest_time', 'video_url', 'image', 'instructions', 'tips', 'created_at']
        read_only_fields = ['id', 'target_muscle', 'muscles_secondary', 'instructions', 'tips', 'equipment', 'difficulty', 'created_at']