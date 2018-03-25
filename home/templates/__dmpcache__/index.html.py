# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521939627.544628
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
        str = context.get('str', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        top_blogs = context.get('top_blogs', UNDEFINED)
        recent_blogs = context.get('recent_blogs', UNDEFINED)
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
        str = context.get('str', UNDEFINED)
        def top_content():
            return render_top_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        top_blogs = context.get('top_blogs', UNDEFINED)
        recent_blogs = context.get('recent_blogs', UNDEFINED)
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
        __M_writer('</div>\n\n<div id="category_div_wrap">\n   <h2>Categories</h2>\n   <ul>\n')
        for c in categories:
            __M_writer('         <li>\n            <a href="/category/')
            __M_writer(str( c.name ))
            __M_writer('">\n               <div class="category_div">\n                     <p class="category_name">')
            __M_writer(str( c.name ))
            __M_writer('</p>\n                     <!--<p class="category_description">')
            __M_writer(str( b.description ))
            __M_writer('</p>-->\n               </div>\n            </a>\n         </li>\n')
        __M_writer('   </ul>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"17": 2, "30": 0, "42": 1, "43": 2, "48": 64, "54": 3, "65": 3, "66": 5, "67": 5, "68": 7, "69": 7, "70": 7, "71": 7, "72": 7, "73": 10, "74": 10, "75": 11, "76": 11, "77": 12, "78": 12, "79": 18, "80": 19, "81": 19, "82": 19, "83": 21, "84": 21, "85": 21, "86": 21, "87": 21, "88": 23, "89": 23, "90": 24, "91": 24, "92": 25, "93": 25, "94": 30, "95": 34, "96": 35, "97": 35, "98": 35, "99": 37, "100": 37, "101": 37, "102": 37, "103": 37, "104": 39, "105": 39, "106": 40, "107": 40, "108": 41, "109": 41, "110": 46, "111": 51, "112": 52, "113": 53, "114": 53, "115": 55, "116": 55, "117": 56, "118": 56, "119": 61, "125": 119}}
__M_END_METADATA
"""
