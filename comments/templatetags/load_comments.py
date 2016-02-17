#coding:utf-8
from django import template
from comments.models import Comment
register = template.Library()

def comments_list(objclass_str, objid_id, flag):
    '''ruce为True，则进行递归，显示评论的回复'''
    comments = Comment.objects.filter(objclass=objclass_str, objid=objid_id)
    return {'comments': comments, 'recu': flag}
register.inclusion_tag('comments/comments_list.html')(comments_list)

def comments_form(objclass_str, objid_id):
    return {'objclass': objclass_str, 'objid': objid_id}
register.inclusion_tag('comments/comments_form.html')(comments_form)
