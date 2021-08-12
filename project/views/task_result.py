from rest_framework import viewsets
from django_celery_results.models import TaskResult
from project.serializers import TaskResultSerializer


class TaskResultViewSet(viewsets.ModelViewSet):
    queryset = TaskResult.objects.all().order_by('-date_created')
    serializer_class = TaskResultSerializer
