# Generated by Django 3.1.13 on 2021-09-10 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20210910_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenkinsjob',
            name='env',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.env', verbose_name='环境'),
        ),
        migrations.AlterField(
            model_name='jenkinsjob',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.project', verbose_name='项目'),
        ),
    ]
