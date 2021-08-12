from django.db import models
from django.utils import timezone


# 主机
class Host(models.Model):
    name = models.CharField('显示名称', max_length=200)
    hostname = models.CharField('主机名', max_length=200, blank=True)
    inside_ip = models.GenericIPAddressField('内网 IP')
    outside_ip = models.GenericIPAddressField('外网 IP', default='0.0.0.0')
    inside_port = models.IntegerField('内网端口号', default=22)
    outside_port = models.IntegerField('外网端口号', default=52113)
    os = models.CharField('系统', max_length=200)
    cpu = models.IntegerField('CPU 核数', default=4)
    memory = models.CharField('内存大小', max_length=10, default='8G')
    disk = models.CharField('硬盘大小', max_length=10, default='80G')
    cloud = models.CharField('云平台', max_length=200)
    cloud_user = models.CharField('云账号', max_length=200, blank=True)
    env = models.CharField('环境', max_length=200, default='test')
    user = models.CharField('用户', max_length=200, default='root')
    password = models.CharField('密码', max_length=200, default='123456')
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        ordering = ['cloud_user', 'env', 'hostname', 'inside_ip']
        unique_together = ['inside_ip', 'cloud_user']
        verbose_name = '主机'
        verbose_name_plural = '主机'

    def __str__(self):
        return self.hostname
