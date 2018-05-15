from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from home import models as hmod


@view_function
def process_request(request, category_url = 'recent'):
    if category_url == 'recent':
        blogs = list(hmod.Blog.objects.all().order_by('id'))[::-1]
    else:
        c = hmod.Category.objects.get(url = category_url)
        blogs = list(hmod.Blog.objects.filter(category_id = c.id).order_by('id'))[::-1]
    context = {
        'blogs': blogs,
    }
    return request.dmp.render('category.html', context)
