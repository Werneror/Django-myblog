from django.contrib import admin
from comments.models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'content', 'date_time')
    class Media:
        js = [
           '/media/editor/tinymce/tinymce.min.js',
           '/media/editor/tinymce/tiny_mce_config.js',
        ]

admin.site.register(Comment, CommentAdmin)
