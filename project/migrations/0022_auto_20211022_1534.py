# Generated by Django 3.1.13 on 2021-10-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20211022_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql',
            name='project',
            field=models.ManyToManyField(to='project.Project', verbose_name='项目'),
        ),
    ]
