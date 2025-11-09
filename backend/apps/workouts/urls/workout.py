from django.urls import path
from ..views.workout_views import CreateWorkout,ListWorkout 

app_name = "workouts"


urlpatterns = [
    path('create/', CreateWorkout.as_view(), name='create-workout'),
    path('list/', ListWorkout.as_view(), name='list-workout'),
    # path('update/<uuid:workout_id>/', UpdateWorkout.as_view(), name='update-workout'),
]
