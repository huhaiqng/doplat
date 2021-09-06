from rest_framework import generics
from django_celery_results.models import TaskResult
from project.serializers import TaskResultSerializer


class TaskResultViewSet(generics.ListAPIView):
    queryset = TaskResult.objects.all().order_by('-date_created')
    serializer_class = TaskResultSerializer
