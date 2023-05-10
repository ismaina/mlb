from django.contrib import admin

from .models import Profile
# admin.site.register(Token, TokenAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "role"]
    list_filter = ["role"]
    list_display_links = ["user"]


admin.site.register(Profile, ProfileAdmin)