from rest_framework import generics
from django.contrib.auth.models import ContentType
from authperm.serializers import ContentTypeSerializer


class ContentTypeViewSet(generics.ListAPIView):
    queryset = ContentType.objects.filter(app_label__in=['app', 'authperm', 'project'])
    serializer_class = ContentTypeSerializer
    pagination_class = None

