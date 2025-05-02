from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at')
    search_fields = ('title', 'content')


admin.site.register(Comment)