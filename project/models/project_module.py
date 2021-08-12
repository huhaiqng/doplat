from django.db import models
from .project import Project


class ProjectModule(models.Model):
    PAG_TYPE_CHOICES = (('jar', 'jar'), ('war', 'war'))

    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='项目', related_name='modules')
    module = models.CharField('模块名', max_length=255)
    pkg_name = models.CharField('包名', max_length=255, blank=True)
    pkg_type = models.CharField('包类型', choices=PAG_TYPE_CHOICES, max_length=255, blank=True)
    port = models.IntegerField('端口号', blank=True)
    deploy_dir = models.CharField('部署路径', max_length=255, blank=True)
    logfile = models.CharField('日志文件', max_length=255, blank=True)

    class Meta:
        unique_together = ['project', 'module']
        ordering = ['project', 'pkg_type', 'module']
        verbose_name = '项目模块'
        verbose_name_plural = '项目模块'
