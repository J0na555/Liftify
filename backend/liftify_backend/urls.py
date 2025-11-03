from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.urls.auths')),
    path('users/', include('apps.users.urls.users')),
    path('workouts/', include('apps.workouts.urls.workout')),
    path('exercise/', include('apps.workouts.urls.exercise')),
    path('schedule/', include('apps.progress.urls.schedule')),
    path('analytics/', include('apps.progress.urls.analytics')),
]
