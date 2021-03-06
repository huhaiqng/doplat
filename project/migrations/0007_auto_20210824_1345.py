# Generated by Django 3.1.13 on 2021-08-24 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_project_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectmodule',
            options={'ordering': ['project', 'pkg_type', 'name'], 'verbose_name': '项目模块', 'verbose_name_plural': '项目模块'},
        ),
        migrations.RenameField(
            model_name='projectmodule',
            old_name='module',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='projectmodule',
            unique_together={('project', 'name')},
        ),
    ]
