from django.db import models


# 环境
class Env(models.Model):
    name = models.CharField('名称', max_length=200)
    alias = models.CharField('简称', max_length=200, blank=True)

    class Meta:
        verbose_name = '环境'
        verbose_name_plural = '环境'

    def __str__(self):
        return self.name
