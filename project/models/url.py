from django.db import models
from .project import Project
from .env import Env


# 地址
class Url(models.Model):
    name = models.CharField('名称', max_length=200)
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.PROTECT, related_name='urls')
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT)
    url = models.URLField('地址', max_length=200, unique=True)
    popular = models.BooleanField('常用的', default=False)

    class Meta:
        ordering = ['project', 'env', 'name']
        verbose_name = '地址大全'
        verbose_name_plural = '地址大全'

    def __str__(self):
        return self.url
