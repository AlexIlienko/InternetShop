from django.contrib import admin
from .models import Category, Product


# Register your models here.
class BdAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image', 'stock', 'available', 'created')
    list_display_links = ('name', 'image')
    search_fields = ('name',)



admin.site.register(Category)
admin.site.register(Product, BdAdmin)
