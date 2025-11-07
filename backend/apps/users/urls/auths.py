from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from ..views.auth_views import RegisterView, LoginView

app_name = "users"

urlpatterns = [
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
