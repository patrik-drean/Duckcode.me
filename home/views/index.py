from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from home import models as hmod


@view_function
def process_request(request):
    recent_blogs = list(hmod.Blog.objects.all().order_by('-id'))[0:6]
    top_blogs = list(hmod.Blog.objects.filter(top_post = True).order_by('-id'))[0:3]
    categories = list(hmod.Category.objects.all().order_by('name'))
    context = {
        'recent_blogs': recent_blogs,
        'top_blogs': top_blogs,
        'categories': categories,
    }
    return request.dmp.render('index.html', context)
