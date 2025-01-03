from django.contrib import admin
from .models import BotUsers

class BotUsersAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'telegram_username', 'full_name')
    search_fields = ('telegram_id', 'telegram_username', 'full_name')
    ordering = ['telegram_id']
    fields = ('telegram_id', 'telegram_username', 'full_name')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['telegram_id']
        return self.readonly_fields

admin.site.register(BotUsers, BotUsersAdmin)
