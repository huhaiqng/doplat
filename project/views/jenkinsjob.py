from rest_framework import viewsets
from rest_framework.response import Response
from project.models import JenkinsJob
from project.serializers import JenkinsJobSerializer, GetJenkinsJobSerializer
from django.core.exceptions import ObjectDoesNotExist


class JenkinsJobViewSet(viewsets.ModelViewSet):
    queryset = JenkinsJob.objects.all()
    filterset_fields = ('project',)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return GetJenkinsJobSerializer
        return JenkinsJobSerializer

    def create(self, request, *args, **kwargs):
        for job in request.data:
            name = job['name']
            url = job['url']
            try:
                obj = JenkinsJob.objects.get(name=name)
                if obj.url != url:
                    obj.url = url
                    obj.save()
            except ObjectDoesNotExist:
                obj = JenkinsJob()
                obj.name = name
                obj.url = url
                obj.save()
        return Response('同步完成')
