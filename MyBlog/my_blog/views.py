from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Post, postQuote
from random import shuffle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    Posts = Post.objects.all()
    Quotes = postQuote.objects.all()
    inPagePost = []
    for i in range(len(Posts)):
        inPagePost.append(Posts[i])
    for i in range(len(Quotes)):
        inPagePost.append(Quotes[i])
    #shuffle(inPagePost)
    lastsPosts = []
    lastestPost = 0
    page = request.GET.get('page',1)
    print(request.GET.get('page',1))
    paginator = Paginator(inPagePost,2)
    try:
        slicedposts = paginator.page(page)
    except PageNotAnInteger:
        slicedposts = paginator.page(0)
    except EmptyPage:
        slicedposts = paginator.page(paginator.num_pages)
    
    for post in Posts:
        if(post.type_of_post !=  'postQuote'):
            if lastestPost == 0:
                lastestPost = post
            elif len(lastsPosts)<2: 
                lastsPosts.append(post)
    c = {
         'posts':slicedposts,
         'lastestPost':lastestPost,
         'lastposts':lastsPosts
         }

    return(render(request, 'index/index.jinja', c))
