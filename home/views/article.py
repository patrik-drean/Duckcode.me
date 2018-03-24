from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from home import models as hmod


@view_function
def process_request(request, article_url = 'how_to_deploy_to_heroku'):
    article = hmod.Blog.objects.get(url = article_url)
    context = {
        'article': article,
    }
    return request.dmp.render('article.html', context)
