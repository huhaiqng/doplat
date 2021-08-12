from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import PopularUrlSerializer
from project.models import Url
from django_filters.rest_framework import DjangoFilterBackend


class PopularUrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.filter(popular=True).order_by('project__name', 'env__name', 'name')
    serializer_class = PopularUrlSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
