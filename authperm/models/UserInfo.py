from django.db import models
from django.contrib.auth.models import AbstractUser


# 自定义用户
class UserInfo(AbstractUser):
    phone = models.CharField('手机号码', max_length=11, unique=True)
    hosted = models.BooleanField('主持早会', default=False)
    hosted_date = models.DateField('主持日期', blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
