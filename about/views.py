#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Classs
from about.models import Aboutme, Aboutblog
from django.core.context_processors import csrf

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    c = {}
    c.update(csrf(request))
    classs = Classs.objects.all()
    return dict( c.items()+{'classification': classs}.items() )

def about(request):
    try:
        aboutme = Aboutme.objects.latest('date_time')
    except :
        aboutme = ''
    try:
        aboutblog = Aboutblog.objects.latest('date_time')
    except :
        aboutblog = ''
    return render_to_response('templates/about.html',
                             {'aboutme':aboutme, 'aboutblog':aboutblog},
                             context_instance=RequestContext(request, processors=[custom_proc]))
