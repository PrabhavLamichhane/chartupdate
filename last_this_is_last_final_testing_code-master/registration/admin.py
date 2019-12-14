from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# admin.site.register(Account)


class AccountAdmin(UserAdmin):
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # ),
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name',
                    'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
