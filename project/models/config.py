from django.db import models
from django.utils import timezone
from .project import Project
from .env import Env


class Config(models.Model):
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.PROTECT)
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT)
    conf = models.TextField('配置')
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ['project', 'env']
        ordering = ['project']
