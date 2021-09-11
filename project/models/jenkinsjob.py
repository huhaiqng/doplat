from django.db import models
from django.utils import timezone
from .project import Project
from .env import Env


class JenkinsJob(models.Model):
    name = models.CharField('名称', unique=True, max_length=255)
    url = models.CharField('地址', max_length=255)
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.PROTECT, blank=True, null=True,
                                related_name='jenkinsjobs')
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField('创建时间', default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ['project', 'env', 'name']
