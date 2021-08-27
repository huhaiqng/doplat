from django.db import models
from django.contrib.auth.models import ContentType
from .l1menu import L1Menu


# 二级菜单
class L2Menu(models.Model):
    parent = models.ForeignKey(L1Menu, on_delete=models.PROTECT, verbose_name='一级菜单', related_name='children')
    title = models.CharField('显示名称', max_length=255)
    content_type = models.ForeignKey(
        ContentType, verbose_name='模型',
        on_delete=models.PROTECT,
        limit_choices_to={'app_label__in': ['app', 'authperm', 'project']},
        blank=True, null=True,
        help_text='绑定模型'
    )
    path = models.CharField('URI', max_length=255, help_text='不需要 /，例如: user')
    component = models.CharField('部件', max_length=255, help_text='相对于 /views 的路径, 例如: /resource/host')
    order = models.IntegerField('排序', default=10, help_text='菜单排序，小的排前面')

    class Meta:
        verbose_name = '二级菜单'
        verbose_name_plural = '二级菜单'
        ordering = ['parent', 'order', 'component']

    def __str__(self):
        return self.title
