# -*- coding: utf-8 -*-
from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(u'标签名', max_length=30)
    tag_explain = models.CharField(u'标签说明', max_length=100, blank=True)
         
    def __unicode__(self):
        return self.tag_name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

class Classs(models.Model):
    classname = models.CharField(u'分类', max_length=30)

    def __unicode__(self):
        return self.classname

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

class Author(models.Model):
    author_name = models.CharField(u'作者', max_length=30)
    email = models.EmailField(u'电子邮箱', blank=True)

    def __unicode__(self):
        return self.author_name
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

class Article(models.Model):
    title = models.CharField(u'标题',max_length=100)
    classification = models.ManyToManyField(Classs, max_length=50)
    tags = models.ManyToManyField(Tag, max_length=50, blank=True)
    authors = models.ManyToManyField(Author, max_length=50)
    content = models.TextField(u'内容', blank=True, null=True)
    date_time = models.DateTimeField(u'日期', auto_now_add=True)

    def __unicode__(self):
        return self.title
                      
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-date_time']
 
class Photo(models.Model):
    title = models.CharField(u'名称', max_length=100)  
    image = models.ImageField(u'图片', upload_to='photos') 
    caption = models.CharField(u'描述', max_length=250, blank=True)
    date_time = models.DateTimeField(u'日期', auto_now_add=True)

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
        ordering = ["-date_time"]
          
    def __unicode__(self):  
        return self.title  
     
    @models.permalink  
    def get_absolute_url(self):  
        return ('photo_detail', None, {'object_id':self.id})
