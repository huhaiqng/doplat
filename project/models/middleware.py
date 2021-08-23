from django.db import models
from .project import Project
from .env import Env
from django.utils import timezone


# 中间件
class Middleware(models.Model):
    conn_addr = models.CharField('连接地址', max_length=200, unique=True)
    web_addr = models.CharField('Web 地址', max_length=200, blank=True)
    username = models.CharField('用户名', max_length=200, blank=True)
    password = models.CharField('密码', max_length=200, blank=True)
    type = models.CharField('类别', max_length=200)
    project = models.ManyToManyField(Project, verbose_name='项目')
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT)
    cluster = models.CharField('集群名', max_length=200, default='单节点')
    created = models.DateTimeField('创建时间', default=timezone.now, blank=True)

    class Meta:
        verbose_name = '中间件'
        verbose_name_plural = verbose_name
        ordering = ['env', 'cluster', 'conn_addr']
