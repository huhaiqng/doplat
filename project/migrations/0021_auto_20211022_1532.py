# Generated by Django 3.1.13 on 2021-10-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_mysql_env'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql',
            name='project',
            field=models.ManyToManyField(blank=True, null=True, to='project.Project', verbose_name='项目'),
        ),
    ]