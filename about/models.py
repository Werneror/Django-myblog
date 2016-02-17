#coding:utf-8
from django.db import models

class Aboutme(models.Model):
    title = models.CharField(u'标题',max_length=100)
    content = models.TextField(u'内容', blank=True, null=True)
    date_time = models.DateTimeField(u'日期', auto_now_add=True)

    def __unicode__(self):
        return self.title
                      
    class Meta:
        verbose_name = '关于我'
        verbose_name_plural = '关于我'
        ordering = ['-date_time']

class Aboutblog(models.Model):
    title = models.CharField(u'标题',max_length=100)
    content = models.TextField(u'内容', blank=True, null=True)
    date_time = models.DateTimeField(u'日期', auto_now_add=True)

    def __unicode__(self):
        return self.title
                      
    class Meta:
        verbose_name = '关于本博客'
        verbose_name_plural = '关于本博客'
        ordering = ['-date_time']
