from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from home import models as hmod


@view_function
def process_request(request):
    context = {
    }
    return request.dmp.render('about.html', context)
