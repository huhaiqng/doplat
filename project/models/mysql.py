from django.db import models
from django.utils import timezone
from .project import Project
from .env import Env


# MySQL 实例
class MySQL(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200, unique=True)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    role = models.CharField('角色', max_length=200)
    data_dir = models.CharField('数据库路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    manager = models.CharField('管理员', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    project = models.ManyToManyField(Project, verbose_name='项目')
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = 'MySQL'
        verbose_name_plural = 'MySQL'
        ordering = ['cluster', 'inside_addr']
