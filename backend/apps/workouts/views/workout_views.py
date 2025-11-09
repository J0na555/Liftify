from ..serializers import WorkoutSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Workout


class CreateListWorkout(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)