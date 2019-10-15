from django.contrib import admin
from .models import Error


class ErrorModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'environment', 'created_at', 'address')


admin.site.register(Error, ErrorModelAdmin)
