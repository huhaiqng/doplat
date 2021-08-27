from django.contrib.auth.models import ContentType
from rest_framework import serializers


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'
