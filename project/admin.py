from django.contrib import admin
from project.models import Project, Url, Env, BuildHost, ProjectModule, Host
from guardian.admin import GuardedModelAdmin


class ProjectAdmin(GuardedModelAdmin):
    list_display = ('name', 'alias', 'user', 'deploy_dir', 'log_dir', 'used')


class ProjectModuleAdmin(GuardedModelAdmin):
    list_display = ('project', 'module', 'pkg_name', 'pkg_type', 'port', 'deploy_dir', 'logfile')


class BuildHostAdmin(GuardedModelAdmin):
    list_display = ('project', 'host', 'env', 'user')


class ProjectUrlAdmin(GuardedModelAdmin):
    list_display = ('project', 'name', 'env', 'url', 'popular')


class HostAdmin(GuardedModelAdmin):
    list_display = ('name', 'hostname', 'inside_ip', 'outside_ip', 'cloud', 'cloud_user', 'env')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Env)
admin.site.register(Host, HostAdmin)
admin.site.register(Url, ProjectUrlAdmin)
admin.site.register(BuildHost, BuildHostAdmin)
admin.site.register(ProjectModule, ProjectModuleAdmin)
