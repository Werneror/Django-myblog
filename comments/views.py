#coding:utf-8
from blog.models import Article
from blog.models import Classs
from comments.models import Comment
from django.core.context_processors import csrf
from django.http import HttpResponse

def comment_app(request):
    if request.method == 'POST':
        c_author = request.POST['author']
        c_email = request.POST['email']
        c_url = request.POST['url']
        c_content = request.POST['content']
        c_obj_class = request.POST['obj_class']
        try:
            c_obj_id = int(request.POST['obj_id'])
        except ValueError:
            raise Http404()
        p = Comment(author=c_author, email=c_email, url=c_url, content=c_content, objclass=c_obj_class, objid=c_obj_id)
        p.save()
    return HttpResponse("评论成功，请返回并刷新页面。")
