# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1524262618.791838
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
        

        __M_writer('\n<!--\n* import image\n*\n-->\n')
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
        __M_writer('</p>\n\n   <div id=\'article_content\'>\n     <h2>Quick Start</h2>\n     <p>Check out this\n       <a href=\'https://codepen.io/pdrean4/pen/KRprzN\' target=\'_blank\'>\n         CodePen\n       </a>\n       to see the five star review in action. The comments there may be all you need.</p>\n\n     <h2>HTML</h2>\n     <figure>\n      <pre>\n      <code class=\'language-html line-numbers\' contenteditable spellcheck=\'false\' >\n<xmp>\n<!-- Import svg library from FontAwesome  -->\n<script defer src=\'https://use.fontawesome.com/releases/v5.0.7/js/all.js\'></script>\n\n<div class=\'row\' id=\'star_div\'>\n         <div class=\'star_wrap 1\'><i class=\'far fa-star fa-2x stars\'></i></div>\n         <div class=\'star_wrap 2\'><i class=\'far fa-star fa-2x stars\'></i></div>\n         <div class=\'star_wrap 3\'><i class=\'far fa-star fa-2x stars\'></i></div>\n         <div class=\'star_wrap 4\'><i class=\'far fa-star fa-2x stars\'></i></div>\n         <div class=\'star_wrap 5\'><i class=\'far fa-star fa-2x stars\'></i></div>\n</div>\n\n<input id=\'id_rating\' type=\'hidden\'/>\n</xmp>\n\n      </code>\n      </pre>\n      </figure>\n\n      <p>Be sure to import\n        <a href=\'https://fontawesome.com/how-to-use/svg-with-js\' target=\'_blank\'>\n          FontAwesome</a>.\n        This allows us to use the star svg icon.\n      </p>\n      <p>\n        The class \'star_wrap\' is used for when the mouse hovers over that area.\n      </p>\n      <p>\n        The number class (e.g., \'1\', \'2\') is used so the JavaScript\n        knows which star to stop on depending on the star the user hovers over/clicks.\n      </p>\n      <p>\n        The hidden field\'s value will change depending on the star selected. The\n          <a href=\'https://codepen.io/pdrean4/pen/KRprzN\' target=\'_blank\'>\n            CodePen\n          </a> demonstrates that.\n        </thead>\n      </p>\n\n    <h2>CSS</h2>\n\n      <figure>\n       <pre>\n       <code class=\'language-css line-numbers\' contenteditable spellcheck=\'false\' >\n        #star_div {\n           margin: 0 auto;\n           width: 300px;\n        }\n        .star_wrap {\n           padding: 0 10px;\n           float: left;\n        }\n        svg {\n           background-color: inherit;\n           color: #FDE338; // The star color can be changed here\n        }\n\n\n       </code>\n       </pre>\n       </figure>\n\n     <h2 class=\'small_margin\'>JavaScript</h2>\n\n       <figure>\n       <pre>\n       <code class=\'language-javascript line-numbers\' contenteditable spellcheck=\'false\' >\n         // Grab the star wraps and put into a list\n         var stars_wrap = $(\'.star_wrap\');\n\n         // Highlight the color when hovered\n         stars_wrap.hover(\n           function() {\n\n             // Grab the number class in the star wrap the user is on (e.g., "1", "5")\n             var starNumber = ($(this).attr(\'class\').split(/\\s+/))[1];\n\n             // Add color when mouse enters. See below for function.\n             hoverStars(starNumber)\n           }, function() {\n\n             // Take away color when mouse leaves. See below for function.\n             unHoverStars();\n           }\n         );\n\n         // Fill the color when clicked\n         stars_wrap.click(function() {\n\n           // Grab the number class in the star wrap the user is on (e.g., "1", "5")\n           var starNumber = ($(this).attr(\'class\').split(/\\s+/))[1];\n\n           // Keep color added when user clicks. Changes the value of the input with the id of \'rating\'. See below for function.\n           clickStars(starNumber);\n\n           // Takes away events so that user can\'t hover stars anymore\n           stars_wrap.off(\'mouseenter mouseleave\');\n         });\n\n         // The color fill for the svg tags\n\n         var colorFilled = \'M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7\n          54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2\n          12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2\n          316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z\'\n\n         var colorOutlined = \'M528.1 171.5L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4\n         0L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3\n         23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5\n         105.7-103c19-18.5 8.5-50.8-17.7-54.6zM388.6 312.3l23.7 138.4L288 385.4l-124.3\n         65.3 23.7-138.4-100.6-98 139-20.2 62.2-126 62.2 126 139 20.2-100.6 98z\'\n\n         // Functions to hover, unhover, and click\n\n         function hoverStars(starNumber) {\n\n           // Grab each star and put into list\n            var stars = $(\'path\')\n            stars.each(function( index, element ) {\n\n            // Change the \'d\' attribute to fill the color\n            stars_wrap = $(this).parent().parent()\n             $( element ).attr(\'d\', colorFilled);\n\n             // Break the loop once on the hovered star\n             if ( stars_wrap.hasClass(starNumber)) {\n               return false;\n             }\n           });\n\n         }\n         function unHoverStars() {\n\n           // Grab each star and put into list\n            var stars = $(\'path\')\n\n           // Change the \'d\' attribute to be outlined again\n            stars.attr(\'d\', colorOutlined);\n         }\n\n         function clickStars(starNumber) {\n\n           // Grab each star and put into list\n            var stars = $(\'path\')\n            var booleanStar = true\n\n            // Go through each star to give its color until it hits the indicated star\n            stars.each(function( index, element ) {\n\n            if (booleanStar)\n            {\n                $( element ).attr(\'d\', colorFilled);\n\n                stars_wrap = $(this).parent().parent();\n\n                // Determine if this is the star the user is clicking. Change input field\n                if ( stars_wrap.hasClass(starNumber))\n                {\n                   rating = $(\'#rating\')\n                  console.log(rating)\n                   rating.val(starNumber);\n\n                   booleanStar = false;\n                }\n            }\n\n            // Fill in the rest of the stars with outlines once the class was found\n            else\n            {\n                $( element ).attr(\'d\', colorOutlined);\n            }\n         });\n         }\n       </code>\n       </pre>\n       </figure>\n       <p>\n         Make sure you have linked\n         <a href=\'https://www.w3schools.com/jquery/jquery_get_started.asp\' target=\'_blank\'>\n           jQuery\n         </a>\n         in your project.\n       </p>\n       <p>\n         <a href=\'https://twitter.com/patrik_drean\' target=\'_blank\'>\n           Reach out\n         </a>\n         if you have questions.\n       </p>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/article.html", "uri": "article.html", "source_encoding": "utf-8", "line_map": {"28": 0, "43": 1, "48": 3, "53": 6, "58": 11, "63": 220, "69": 3, "76": 3, "82": 4, "89": 4, "90": 5, "91": 5, "97": 8, "105": 8, "106": 9, "107": 9, "108": 9, "109": 9, "110": 9, "116": 12, "123": 12, "124": 13, "125": 13, "126": 15, "127": 15, "133": 127}}
__M_END_METADATA
"""
