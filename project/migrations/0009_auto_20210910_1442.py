# Generated by Django 3.1.13 on 2021-09-10 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_jenkinsjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenkinsjob',
            name='env',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='project.env', verbose_name='环境'),
        ),
        migrations.AlterField(
            model_name='jenkinsjob',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='project.project', verbose_name='项目'),
        ),
    ]
