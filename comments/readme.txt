在需要引入评论的页面加入以下css和js
	<link rel="stylesheet" type="text/css" href="/media/css/comments_form.css">
	<script type="text/javascript" src="/media/js/comments_form.js"></script>
	<!--引入wangEditor.css-->
	<link rel="stylesheet" type="text/css" href="/media/editor/wangEditor-2.0.4/dist/css/wangEditor.min.css">
	<!--引入jquery和wangEditor.js-->   <!--注意：javascript必须放在body最后，否则可能会出现问题-->
	<script type="text/javascript" src="/media/editor/wangEditor-2.0.4/dist/js/lib/jquery-1.10.2.min.js"></script>
	<script type="text/javascript" src="/media/editor/wangEditor-2.0.4/dist/js/wangEditor.min.js"></script>
在需要引入评论的页面加入以下标签
	{% load load_comments %}
    <div class="comments">
        <p class="comments-title">评论：</p>
        <div class="comments-list">
			{% comments_list "article" article.id True %}
        </div>
        <div class="comments-form">
        	{% comments_form "article" article.id %}
        </div>
    </div>
