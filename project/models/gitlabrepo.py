from django.db import models
from django.utils import timezone
from .project import Project


class GitlabRepo(models.Model):
    id = models.IntegerField('id', primary_key=True)
    path_with_namespace = models.CharField('路径', max_length=255)
    description = models.CharField('备注', max_length=255, blank=True, null=True)
    http_url_to_repo = models.URLField('地址')
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.PROTECT, blank=True, null=True,
                                related_name='gitlabrepo')
    created_at = models.DateTimeField('创建时间', default=timezone.now, blank=True, null=True)
    last_activity_at = models.DateTimeField('创建时间', default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ['project', 'path_with_namespace']
