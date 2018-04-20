# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1524263553.002251
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/article.html'
_template_uri = 'article.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'meta_description', 'top_content', 'middle_content']


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
        def meta_description():
            return render_meta_description(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        article = context.get('article', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta_description'):
            context['self'].meta_description(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n<!--\n* import image\n*\n\n')
        __M_writer(str( article.content ))
        __M_writer('\n-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        article = context.get('article', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( article.nav_title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_description(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta_description():
            return render_meta_description(context)
        article = context.get('article', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str( article.meta_description))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content():
            return render_top_content(context)
        article = context.get('article', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n   <img id='main_img' src='")
        __M_writer(str( STATIC_URL ))
        __M_writer(str(article.image_url()))
        __M_writer("' alt='")
        __M_writer(str( article.alt_text))
        __M_writer("' />\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middle_content():
            return render_middle_content(context)
        article = context.get('article', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <h1>')
        __M_writer(str( article.title ))
        __M_writer("</h1>\n   <p id='article_author'>by Patrik Drean</p>\n   <p id='article_datestamp'>")
        __M_writer(str( article.create_date.strftime('%B %d, %Y') ))
        __M_writer("</p>\n\n   <div id='article_content'>\n      ")
        __M_writer(str( article.content ))
        __M_writer('\n   </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/article.html", "uri": "article.html", "source_encoding": "utf-8", "line_map": {"28": 0, "43": 1, "48": 3, "53": 6, "58": 11, "63": 20, "64": 25, "65": 25, "71": 3, "78": 3, "84": 4, "91": 4, "92": 5, "93": 5, "99": 8, "107": 8, "108": 9, "109": 9, "110": 9, "111": 9, "112": 9, "118": 12, "125": 12, "126": 13, "127": 13, "128": 15, "129": 15, "130": 18, "131": 18, "137": 131}}
__M_END_METADATA
"""
