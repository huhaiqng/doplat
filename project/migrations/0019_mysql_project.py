# Generated by Django 3.1.13 on 2021-10-22 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_url_public_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysql',
            name='project',
            field=models.ManyToManyField(to='project.Project', verbose_name='项目'),
        ),
    ]
