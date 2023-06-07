from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'uuid','image', 'message', 'supported', 'created_at')
    list_filter = ('created_at','supported',)
    search_fields = ['first_name', 'last_name', 'message', 'created_at']

admin.site.register(Contact, ContactAdmin)