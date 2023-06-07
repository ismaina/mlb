from django.contrib import admin

from .models import Product, Category



class ProductAdmin(admin.ModelAdmin):
    list_display = ('code','title','slug', 'description', 'price', 'datetime')
    list_filter = ('title',)
    # readonly_fields = ('submitted',)
    search_fields = ('title', 'description',)

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'datetime')
    list_filter = ('title',)
    # readonly_fields = ('submitted',)
    search_fields = ('title', 'description',)

admin.site.register(Category, CategoryAdmin)