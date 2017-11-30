from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from .models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
#def index(response):
#    view = 'template_two'
#    return render_to_response('blog_shad/index.html', {'name':view})

def articles(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list,4)

    page = request.GET.get('page')
    try:
        article1 = paginator.page(page)
    except PageNotAnInteger:
        article1 = paginator.page(1)
    except EmptyPage:
        article1 = paginator.page(paginator.num_pages)
    return render_to_response('templates/articles.html',
                            {
                            'article1':article1,
                            'articles':Article.objects.all(),
                            'username_status': auth.get_user(request).is_authenticated,
                            'username' : auth.get_user(request)
                            })


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    paginator = Paginator(Comments.objects.filter(comment_article_id=article_id),4)
    page = request.GET.get('comm')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    args['article'] = Article.objects.get(id = article_id)
    args['comments'] = comments

    args['form'] = comment_form
    args['username'] = auth.get_user(request)
    args['username_status'] = auth.get_user(request).is_authenticated
    return render_to_response('article.html', args)


def addlike(request, article_id=1):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id = article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST: #and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment_text']

            comment_auth = Comments.objects.create(comment_text = comment, comment_author = auth.get_user(request), comment_article = Article.objects.get(id = article_id) )
            #comment.comment_article = Article.objects.get(id = article_id)
            #form.save()

            request.session.set_expiry(60)
            request.session['pause'] = True

    return redirect('/article/%s/' % article_id )

def contacts(request):

    return render_to_response('contacts.html')