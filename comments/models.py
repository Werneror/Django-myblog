#coding:utf-8
from django.db import models

# Create your models here.
class Comment(models.Model):
    objclass = models.CharField(u'对象类型', max_length=50)
    objid = models.IntegerField(u'对象ID')
    email = models.EmailField(u'电子邮箱')
    author = models.CharField(u'作者', max_length=50)
    url = models.URLField(u'网站', blank=True)
    content = models.TextField(u'内容', null=True)
    date_time = models.DateTimeField(u'日期', auto_now_add=True)

    def __unicode__(self):
        return self.author

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-date_time']
