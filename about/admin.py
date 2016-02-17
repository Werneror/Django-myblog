from django.contrib import admin
from about.models import Aboutme, Aboutblog

class TextAdmin(admin.ModelAdmin):
    list_display = ('title','date_time')
    class Media:
        js = [
           '/media/editor/kindeditor-4.1.10/kindeditor.js',
           '/media/editor/kindeditor-4.1.10/lang/zh_CN.js',
           '/media/editor/kindeditor-4.1.10/use.js',
        ]

admin.site.register(Aboutme, TextAdmin)
admin.site.register(Aboutblog, TextAdmin)
