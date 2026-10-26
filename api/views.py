from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
def hello(request):
    """GET /api/hello/ - simple endpoint used to show a change going live."""
    return Response({"message": "Hello from CSC325!", "status": "ok"})


class TaskViewSet(viewsets.ModelViewSet):
    """CRUD endpoints at /api/tasks/."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
