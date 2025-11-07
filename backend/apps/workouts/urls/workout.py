from django.urls import path
from ..views.workout_views import CreateWorkout

app_name = "workouts"


urlpatterns = [
    path('create/', CreateWorkout.as_view(), name='create-workout'),
]
