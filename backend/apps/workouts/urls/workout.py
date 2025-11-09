from django.urls import path
from ..views.workout_views import CreateListWorkout

app_name = "workouts"


urlpatterns = [
    path('create/', CreateListWorkout.as_view(), name='create-workout'),
    path('list/', CreateListWorkout.as_view(), name='list-workouts'),
]
