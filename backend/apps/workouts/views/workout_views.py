import uuid
from ..serializers import WorkoutSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Workout


class CreateWorkout(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListWorkout(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

class UpdateWorkout(generics.RetrieveUpdateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'



