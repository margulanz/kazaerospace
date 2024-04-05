from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Trainer, Client


class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['is_trainer'] = forms.BooleanField()


class UserAdmin(UAdmin):
    list_display = ['username', 'first_name', 'last_name', 'sex', 'is_trainer']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'last_name', 'email', 'sex')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )


UserAdmin.add_form(UserCreationFormExtended)
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'is_trainer', 'password1', 'password2',)
    }),
)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'sex']
    readonly_fields = ('user',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def username(self, obj):
        return obj.user.username
    # username.admin_order_field = 'user'

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def sex(self, obj):
        return obj.user.sex


class ClientAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'sex']
    readonly_fields = ('user',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def sex(self, obj):
        return obj.user.sex


admin.site.register(User, UserAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Client, ClientAdmin)
