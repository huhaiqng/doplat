from rest_framework import viewsets, status
from rest_framework.response import Response
from project.models import GitlabRepo
from project.serializers import GitlabRepoSerializer, GetGitlabRepoSerializer
from django.core.exceptions import ObjectDoesNotExist
from project.filters import GitlabRepoFilter


class GitlabRepoViewSet(viewsets.ModelViewSet):
    queryset = GitlabRepo.objects.all()
    filterset_class = GitlabRepoFilter

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return GetGitlabRepoSerializer
        return GitlabRepoSerializer

    def create(self, request, *args, **kwargs):
        for repo in request.data:
            try:
                partial = kwargs.pop('partial', False)
                instance = GitlabRepo.objects.get(pk=repo['id'])
                serializer = self.get_serializer(instance, data=repo, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}
            except ObjectDoesNotExist:
                serializer = self.get_serializer(data=repo)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
        return Response('同步完成')
