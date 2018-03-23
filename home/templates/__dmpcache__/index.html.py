# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521817644.7269602
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content']


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
        recent_blogs = context.get('recent_blogs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        top_blogs = context.get('top_blogs', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        recent_blogs = context.get('recent_blogs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        top_blogs = context.get('top_blogs', UNDEFINED)
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div id="highlight_blog_div">\n   <img id="highlight_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer(str(recent_blogs[-1].image_url()))
        __M_writer('" alt="')
        __M_writer(str( recent_blogs[-1].alt_text))
        __M_writer('"/>\n   <div id="highlight_message_div">\n      <p id="highlight_featured_post">Featured Post</p>\n      <h1>')
        __M_writer(str( recent_blogs[-1].title ))
        __M_writer('</h1>\n      <p id="highlight_datestamp">by Patrik Drean - 3 hours ago</p>\n      <p id="highlight_description">')
        __M_writer(str( recent_blogs[-1].description ))
        __M_writer('</p>\n   </div>\n</div>\n\n<div id="top_blog_div">\n   <h2>Top Posts</h2>\n')
        for b in top_blogs:
            __M_writer('      <div class="top_blog_div">\n         <img class="top_img" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( b.image_url()))
            __M_writer('" alt="')
            __M_writer(str( b.alt_text))
            __M_writer('"/>\n         <div class="top_message_div">\n            <h2>')
            __M_writer(str( b.title ))
            __M_writer('</h2>\n            <p class="top_datestamp">by Patrik Drean - 3 hours ago</p>\n            <p class="top_description">')
            __M_writer(str( b.description ))
            __M_writer('</p>\n         </div>\n      </div>\n')
        __M_writer('</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 29, "49": 3, "58": 3, "59": 6, "60": 6, "61": 6, "62": 6, "63": 6, "64": 9, "65": 9, "66": 11, "67": 11, "68": 17, "69": 18, "70": 19, "71": 19, "72": 19, "73": 19, "74": 19, "75": 21, "76": 21, "77": 23, "78": 23, "79": 27, "85": 79}}
__M_END_METADATA
"""
