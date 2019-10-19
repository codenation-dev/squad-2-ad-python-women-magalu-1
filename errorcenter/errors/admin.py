from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import User, Error


class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date_joined', 'is_active', 
        'is_superuser', 'is_staff'
    )


class ErrorModelAdmin(admin.ModelAdmin):
    def related_user(self, obj):
        href = reverse('admin:errors_user_change', args=(obj.user.pk,))
        return format_html(f'<a href="{ href }">{ obj.user }</a>')

    related_user.short_description = 'Usuário'

    list_display = (
        'title', 'level', 'environment', 
        'created_at', 'address', 'related_user'
    )


admin.site.register(User, UserModelAdmin)
admin.site.register(Error, ErrorModelAdmin)
