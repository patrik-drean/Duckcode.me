# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521922201.246737
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content']


from home import duck_time_past as dtp

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
        def top_content():
            return render_top_content(context._locals(__M_locals))
        recent_blogs = context.get('recent_blogs', UNDEFINED)
        str = context.get('str', UNDEFINED)
        top_blogs = context.get('top_blogs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        recent_blogs = context.get('recent_blogs', UNDEFINED)
        str = context.get('str', UNDEFINED)
        top_blogs = context.get('top_blogs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<a href="/article/')
        __M_writer(str( recent_blogs[0].url ))
        __M_writer('">\n   <div id="highlight_blog_div">\n      <img id="highlight_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer(str(recent_blogs[0].image_url()))
        __M_writer('" alt="')
        __M_writer(str( recent_blogs[0].alt_text))
        __M_writer('" />\n      <div id="highlight_message_div">\n         <p id="highlight_featured_post">Featured Post</p>\n         <h1>')
        __M_writer(str( recent_blogs[0].title ))
        __M_writer('</h1>\n         <p id="highlight_datestamp">by Patrik Drean - ')
        __M_writer(str( dtp.past_time(str(recent_blogs[0].create_date)) ))
        __M_writer('</p>\n         <p id="highlight_description">')
        __M_writer(str( recent_blogs[0].description ))
        __M_writer('</p>\n      </div>\n   </div>\n</a>\n<div id="top_blog_div_wrap">\n   <h2>Popular Posts</h2>\n')
        for b in top_blogs:
            __M_writer('      <a href="/article/')
            __M_writer(str( b.url ))
            __M_writer('">\n         <div class="top_blog_div">\n            <img class="top_img" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( b.image_url()))
            __M_writer('" alt="')
            __M_writer(str( b.alt_text))
            __M_writer('"/>\n            <div class="top_message_div">\n               <h3>')
            __M_writer(str( b.title ))
            __M_writer('</h3>\n               <p class="top_datestamp">by Patrik Drean - ')
            __M_writer(str( dtp.past_time(str(b.create_date)) ))
            __M_writer('</p>\n               <p class="top_description">')
            __M_writer(str( b.description ))
            __M_writer('</p>\n            </div>\n         </div>\n      </a>\n')
        __M_writer('</div>\n\n<div id="recent_blog_div_wrap">\n   <h2>Recent Posts</h2>\n')
        for b in recent_blogs:
            __M_writer('      <a href="/article/')
            __M_writer(str( b.url ))
            __M_writer('">\n         <div class="recent_blog_div">\n            <img class="recent_img" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( b.image_url()))
            __M_writer('" alt="')
            __M_writer(str( b.alt_text))
            __M_writer('"/>\n            <div class="recent_message_div">\n               <h3>')
            __M_writer(str( b.title ))
            __M_writer('</h3>\n               <p class="recent_datestamp">by Patrik Drean - ')
            __M_writer(str( dtp.past_time(str(b.create_date)) ))
            __M_writer('</p>\n               <p class="recent_description">')
            __M_writer(str( b.description ))
            __M_writer('</p>\n            </div>\n         </div>\n      </a>\n')
        __M_writer('</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"17": 2, "30": 0, "41": 1, "42": 2, "47": 48, "53": 3, "63": 3, "64": 5, "65": 5, "66": 7, "67": 7, "68": 7, "69": 7, "70": 7, "71": 10, "72": 10, "73": 11, "74": 11, "75": 12, "76": 12, "77": 18, "78": 19, "79": 19, "80": 19, "81": 21, "82": 21, "83": 21, "84": 21, "85": 21, "86": 23, "87": 23, "88": 24, "89": 24, "90": 25, "91": 25, "92": 30, "93": 34, "94": 35, "95": 35, "96": 35, "97": 37, "98": 37, "99": 37, "100": 37, "101": 37, "102": 39, "103": 39, "104": 40, "105": 40, "106": 41, "107": 41, "108": 46, "114": 108}}
__M_END_METADATA
"""
