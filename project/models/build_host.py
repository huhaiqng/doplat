from django.db import models
from .host import Host
from .env import Env
from .project import Project


class BuildHost(models.Model):
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.PROTECT)
    host = models.ForeignKey(Host, verbose_name='主机', on_delete=models.PROTECT)
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT)
    user = models.CharField('打包用户', max_length=200, default='www')

    class Meta:
        unique_together = ['project', 'env']
        verbose_name = '打包主机'
        verbose_name_plural = '打包主机'

    def __str__(self):
        return self.project.name
