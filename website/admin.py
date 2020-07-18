from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'status', 'data_publicacao',  'slug')
    search_fields = ['titulo']
    prepopulated_fields = {"slug": ("titulo",)}


admin.site.register(Post, PostAdmin)
