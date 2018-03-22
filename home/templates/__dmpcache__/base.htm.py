# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521690990.546945
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content', 'left_content', 'middle_content', 'right_content', 'footer_content']


import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def footer_content():
            return render_footer_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n      ')
        __M_writer('\n        <title>Pat\'s Template</title>\n\n       <!-- Bootstrap CSS link -->\n       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n\n      <nav id = \'nav\' class="navbar navbar-toggleable-md navbar-inverse bg-inverse">\n     <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">\n      <span class="navbar-toggler-icon"></span>\n     </button>\n     <a class="navbar-brand" href="/">\n        <img id=\'duck_logo\' src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/home/media/img/duck_logo.png" />\n     </a>\n\n     <div class="collapse navbar-collapse" id="navbarsExampleDefault">\n      <ul class="navbar-nav mr-auto">\n         <li class="nav-item">\n           <a class="nav-link" href="#">Home</a>\n         </li>\n         <li class="nav-item">\n           <a class="nav-link" href="#">About</a>\n         </li>\n         <li class="nav-item">\n           <a class="nav-link" href="#">Contact</a>\n         </li>\n      </ul>\n      <!-- <form class="form-inline my-2 my-md-0">\n         <input class="form-control mr-sm-2" placeholder="Search" type="text">\n         <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>\n      </form> -->\n      <div class="nav-item dropdown ">\n        <a class="nav-link dropdown-toggle" href="http://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Login</a>\n        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdown01">\n          <a class="dropdown-item" href="#">Login</a>\n          <a class="dropdown-item" href="#">Signup</a>\n        </div>\n     </div>\n     </div>\n  </nav>\n\n        <main>\n         <div class="row">\n           <div class="col-md-12" id="top-section">\n             ')
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
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 6, "19": 0, "36": 2, "37": 6, "38": 13, "39": 16, "40": 17, "41": 17, "42": 27, "43": 27, "48": 59, "53": 64, "58": 67, "63": 70, "68": 75, "74": 59, "85": 64, "96": 67, "107": 70, "118": 75, "129": 118}}
__M_END_METADATA
"""
