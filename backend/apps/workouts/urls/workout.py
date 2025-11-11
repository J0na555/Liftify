from django.urls import path
from ..views.workout_views import CreateWorkout,ListWorkout , UpdateWorkout, DeleteWorkout

app_name = "workouts"


urlpatterns = [
    path('create/', CreateWorkout.as_view(), name='create-workout'),
    path('list/', ListWorkout.as_view(), name='list-workout'),
    path('update/<uuid:pk>/', UpdateWorkout.as_view(), name='update-workout'),
    path('delete/<uuid:pk>/', DeleteWorkout.as_view(), name='delete-workout'),
]
