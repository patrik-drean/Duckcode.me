# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1524257409.8129148
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'meta_description', 'top_content', 'left_content', 'middle_content', 'right_content', 'footer_content']


import datetime 

from home import models as hmod 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def meta_description():
            return render_meta_description(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def top_content():
            return render_top_content(context._locals(__M_locals))
        def footer_content():
            return render_footer_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n      <!-- Global site tag (gtag.js) - Google Analytics -->\n      <script async src="https://www.googletagmanager.com/gtag/js?id=UA-100806632-3"></script>\n      <script>\n        window.dataLayer = window.dataLayer || [];\n        function gtag(){dataLayer.push(arguments);}\n        gtag(\'js\', new Date());\n\n        gtag(\'config\', \'UA-100806632-3\');\n      </script>\n      ')
        __M_writer('\n      ')
        __M_writer('\n      ')
        catagories = hmod.Category.objects.all() 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['catagories'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n        <title>\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(' - Duck Code\n        </title>\n        <meta name="description" content="')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta_description'):
            context['self'].meta_description(**pageargs)
        

        __M_writer('">\n        <meta charset="UTF-8">\n        <meta name="viewport" content="width=device-width,initial-scale=1.0">\n       <!-- Bootstrap CSS link -->\n       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">\n\n')
        __M_writer('        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js" ></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n<nav id=\'nav\' class="navbar navbar-toggleable-sm navbar-light">\n  <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">\n      <span class="navbar-toggler-icon"></span>\n     </button>\n  <a class="navbar-brand" href="/">\n        <img id=\'duck_logo\' src="')
        __M_writer(str(STATIC_URL))
        __M_writer('home/media/img/duck_logo.png" />\n     </a>\n  <div class="collapse navbar-collapse" id="navbarsExampleDefault">\n    <ul class="navbar-nav mr-auto">\n      <li class="nav-item">\n        <a class="nav-link" href="/category/recent">All Posts</a>\n      </li>\n      <li class="nav-item dropdown">\n        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Blog Categories</a>\n        <div class="dropdown-menu">\n')
        for c in catagories:
            __M_writer('          <a class="dropdown-item" href="/category/')
            __M_writer(str(c.url))
            __M_writer('">')
            __M_writer(str( c.name ))
            __M_writer('</a>\n')
        __M_writer('        </div>\n      </li>\n      <li class="nav-item">\n        <a class="nav-link" href="/about">About Me</a>\n      </li>\n    </ul>\n  </div>\n</nav>\n\n\n\n        <main>\n         <div class="row">\n           <div class="col-md-12" id="top-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n           </div>\n         </div>\n         <div class="row">\n           <div class="col-md-2" id="left-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\n           </div>\n           <div class="col-md-8" id="middle-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n           </div>\n           <div class="col-md-2" id="right-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\n           </div>\n         </div>\n      </main>\n      <footer>\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_content'):
            context['self'].footer_content(**pageargs)
        

        __M_writer('\n         <p> </p>\n      </footer>\n\n      <!-- Bootstrap JS files -->\n      <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>\n      <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>\n      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_description(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta_description():
            return render_meta_description(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_content():
            return render_footer_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 15, "19": 16, "21": 0, "42": 2, "43": 15, "44": 16, "45": 17, "49": 17, "54": 19, "59": 21, "60": 28, "61": 31, "62": 32, "63": 32, "64": 41, "65": 41, "66": 51, "67": 52, "68": 52, "69": 52, "70": 52, "71": 52, "72": 54, "77": 68, "82": 73, "87": 76, "92": 79, "97": 84, "103": 19, "114": 21, "125": 68, "136": 73, "147": 76, "158": 79, "169": 84, "180": 169}}
__M_END_METADATA
"""
