from django.db import models


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', max_length=20)
    url = models.CharField('地址', max_length=255)
    img = models.CharField('图片', max_length=255, null=True, help_text='例如: /images/abc.jpg')
    order = models.IntegerField('排序', default=100)

    class Meta:
        ordering = ['order']
        verbose_name = '首页地址'
        verbose_name_plural = '首页地址'

    def __str__(self):
        return self.name
