from django.contrib import admin
from .models import UserInfo, L1Menu, L2Menu
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy
from guardian.admin import GuardedModelAdmin


class L1MenuAdmin(GuardedModelAdmin):
    list_display = ('name', 'title', 'icon', 'path', 'redirect', 'order')


class L2MenuAdmin(GuardedModelAdmin):
    list_display = ('title', 'parent', 'path', 'component', 'order')


class UserInfoAdmin(UserAdmin):
    list_display = ('username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined',
                    'hosted', 'hosted_date')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        (gettext_lazy('User Information'), {'fields': ('phone', 'hosted', 'hosted_date')}),

        (gettext_lazy('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                                  'groups', 'user_permissions')}),

        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(L1Menu, L1MenuAdmin)
admin.site.register(L2Menu, L2MenuAdmin)
