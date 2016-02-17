from django.contrib import admin
from blog.models import Tag, Classs, Author, Article, Photo

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date_time')
    class Media:
        js = [
           '/media/editor/kindeditor-4.1.10/kindeditor.js',
           '/media/editor/kindeditor-4.1.10/lang/zh_CN.js',
           '/media/editor/kindeditor-4.1.10/use.js',
        ]

admin.site.register(Tag)
admin.site.register(Classs)
admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Photo)
