from django.contrib import admin
from .models import Address
from guardian.admin import GuardedModelAdmin


class AddressAdmin(GuardedModelAdmin):
    list_display = ('name', 'url', 'order')


admin.site.register(Address, AddressAdmin)
