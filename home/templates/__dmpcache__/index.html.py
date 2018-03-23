# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521822801.310085
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        recent_blogs = context.get('recent_blogs', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        top_blogs = context.get('top_blogs', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        recent_blogs = context.get('recent_blogs', UNDEFINED)
        def top_content():
            return render_top_content(context)
        top_blogs = context.get('top_blogs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<a href="/">\n   <div id="highlight_blog_div">\n      <img id="highlight_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer(str(recent_blogs[0].image_url()))
        __M_writer('" alt="')
        __M_writer(str( recent_blogs[0].alt_text))
        __M_writer('" />\n      <div id="highlight_message_div">\n         <p id="highlight_featured_post">Featured Post</p>\n         <h1>')
        __M_writer(str( recent_blogs[0].title ))
        __M_writer('</h1>\n         <p id="highlight_datestamp">by Patrik Drean - 3 hours ago</p>\n         <p id="highlight_description">')
        __M_writer(str( recent_blogs[0].description ))
        __M_writer('</p>\n      </div>\n   </div>\n</a>\n<div id="top_blog_div_wrap">\n   <h2>Top Posts</h2>\n')
        for b in top_blogs:
            __M_writer('      <a href="/">\n         <div class="top_blog_div">\n            <img class="top_img" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( b.image_url()))
            __M_writer('" alt="')
            __M_writer(str( b.alt_text))
            __M_writer('"/>\n            <div class="top_message_div">\n               <h3>')
            __M_writer(str( b.title ))
            __M_writer('</h3>\n               <p class="top_datestamp">by Patrik Drean - 3 hours ago</p>\n               <p class="top_description">')
            __M_writer(str( b.description ))
            __M_writer('</p>\n            </div>\n         </div>\n      </a>\n')
        __M_writer('</div>\n\n<div id="recent_blog_div_wrap">\n   <h2>Recent Posts</h2>\n')
        for b in recent_blogs:
            __M_writer('      <a href="/">\n         <div class="recent_blog_div">\n            <img class="recent_img" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( b.image_url()))
            __M_writer('" alt="')
            __M_writer(str( b.alt_text))
            __M_writer('"/>\n            <div class="recent_message_div">\n               <h3>')
            __M_writer(str( b.title ))
            __M_writer('</h3>\n               <p class="recent_datestamp">by Patrik Drean - 3 hours ago</p>\n               <p class="recent_description">')
            __M_writer(str( b.description ))
            __M_writer('</p>\n            </div>\n         </div>\n      </a>\n')
        __M_writer('</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 48, "49": 3, "58": 3, "59": 7, "60": 7, "61": 7, "62": 7, "63": 7, "64": 10, "65": 10, "66": 12, "67": 12, "68": 18, "69": 19, "70": 21, "71": 21, "72": 21, "73": 21, "74": 21, "75": 23, "76": 23, "77": 25, "78": 25, "79": 30, "80": 34, "81": 35, "82": 37, "83": 37, "84": 37, "85": 37, "86": 37, "87": 39, "88": 39, "89": 41, "90": 41, "91": 46, "97": 91}}
__M_END_METADATA
"""
