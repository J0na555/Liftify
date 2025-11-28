from rest_framework import serializers
from .models import Workout, Exercise, WorkoutExercise

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            'id', 'user', 'title', 'status',
            'duration', 'is_public', 'date', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            'id', 'name', 'description',
            'target_muscle', 'muscles_secondary',
            'equipment', 'difficulty', 'category',
            'is_compound', 'video_url', 'image',
            'instructions', 'tips', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_detail = ExerciseSmallSerializer(source='exercise', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = [
            'id',
            'workout',
            'exercise',
            'exercise_detail',
            'sets',
            'reps',
            'weight',
            'duration',
            'distance',
            'rest_time',
            'user_comment',
            'completed',
            'created_at'
        ]

        read_only_fields = ['id', 'created_at', 'exercise_detail']

    def validate(self, data):

        if data.get('sets') is not None and data['sets'] < 0:
            raise serializers.ValidationError("sets can not be negative")

        if data.get('weight') is not None and data['weight'] < 0:
            raise serializers.ValidationError("weight  can not be negative")
        
        if data.get('duration') is not None and data['duration'] < 0:
            raise serializers.ValidationError("Duration  can not be negative")

        if data.get('rest_time') is not None and data['rest_time'] < 0:
            raise serializers.ValidationError("Rest Time  can not be negative")

        if data.get('distance') is not None and data['distance'] < 0:
            raise serializers.ValidationError("Distance cannot be negative.")

        return data
