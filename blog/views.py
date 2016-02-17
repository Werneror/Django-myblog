#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Article
from blog.models import Classs
from blog.models import Photo
from comments.models import Comment
from django.core.context_processors import csrf

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    c = {}
    c.update(csrf(request))
    classs = Classs.objects.all()
    return dict( c.items()+{'classification': classs}.items() )

def homepage(request):
    articles = Article.objects.all()
    return render_to_response('templates/list_all.html', 
                              {'articles': articles}, 
                              context_instance=RequestContext(request, processors=[custom_proc]))

def show_article(request, art_id):
    try:
        art_id = int(art_id)
    except ValueError:
        raise Http404()
    article = Article.objects.get(id=art_id)
    comments = Comment.objects.filter(objclass='article', objid=art_id)
    reply_comments = []
    for comment in comments:
        reply_comment = Comment.objects.filter(objclass='comment', objid=comment.id)
        reply_comments.append(reply_comment)
    return render_to_response('templates/show_article.html',
                              {'article': article, 'comments':comments, 'reply_comments':reply_comments },
                              context_instance=RequestContext(request, processors=[custom_proc]))

def show_class(request, art_id):
    
    try:
        art_id = int(art_id)
    except ValueError:
        raise Http404()
    classname = Classs.objects.get(id=art_id)
    articles = Article.objects.filter(classification=classname)
    return render_to_response('templates/list_by_class.html',
                             {'classname':classname, 'articles': articles},
                             context_instance=RequestContext(request, processors=[custom_proc]))
