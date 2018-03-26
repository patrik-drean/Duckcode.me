# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522075712.1855302
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/article.html'
_template_uri = 'article.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content', 'middle_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        article = context.get('article', UNDEFINED)
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        article = context.get('article', UNDEFINED)
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <img id="main_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer(str(article.image_url()))
        __M_writer('" alt="')
        __M_writer(str( article.alt_text))
        __M_writer('" />\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        article = context.get('article', UNDEFINED)
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <h1>')
        __M_writer(str( article.title ))
        __M_writer('</h1>\n   <p id="article_author">by Patrik Drean</p>\n   <p id="article_datestamp">')
        __M_writer(str( article.create_date.strftime('%B %d, %Y') ))
        __M_writer('</p>\n   <p id="article_content">')
        __M_writer(str( article.content ))
        __M_writer('</p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/article.html", "uri": "article.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 5, "49": 12, "55": 2, "63": 2, "64": 3, "65": 3, "66": 3, "67": 3, "68": 3, "74": 6, "81": 6, "82": 7, "83": 7, "84": 9, "85": 9, "86": 10, "87": 10, "93": 87}}
__M_END_METADATA
"""
