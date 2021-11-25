# Generated by Django 3.1.13 on 2021-09-08 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authperm', '0003_auto_20210824_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='real_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='l1menu',
            name='icon',
            field=models.CharField(default='tree', max_length=255, verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='l2menu',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='authperm.l1menu', verbose_name='一级菜单'),
        ),
    ]
