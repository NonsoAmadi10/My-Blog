from django.contrib import admin
from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug',
                    'created_on', 'cover_image', 'author')
    list_filter = ('status'),
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
