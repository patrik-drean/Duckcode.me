# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522195688.824471
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
        article = context.get('article', UNDEFINED)
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n<!--\n*introduction\n*set-up\n*\n-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        article = context.get('article', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('</p>\n   <!--<div id="article_content">')
        __M_writer(str( article.content))
        __M_writer('</div>-->\n   <div id="article_content">\n     <p>Programming already has its fair share of bugs and headaches. When it comes to\n   deploying a project this pain only multiplies. This is a walkthrough on how to deploy\n   to Heroku when dependencies(e.g., custom frameworks, libraries, etc.) are required for your\n   project. Using <a href=\'http://django-mako-plus.readthedocs.io/about.html\' target=\'_blank\'>\n   Django-Mako-Plus</a>, a custom python framework, we will show how you can deploy your\n   project with a framework that isn\'t officially supported by Heroku.\n </p>\n <h2>Initial Setup</h2>\n\n   <p>\n   <ul>\n     <li>\n       Sign up for a\n       <a href=\'https://signup.heroku.com/dc\' target=\'_blank\'>Heroku</a> account\n     </li>\n     <li>\n       Setup up\n       <a href=\'https://help.github.com/articles/set-up-git/\' target=\'_blank\'>git</a>\n       in your project\n     </li>\n     <li>\n       Install\n       <a href=\'http://www.postgresqltutorial.com/install-postgresql/\' target=\'_blank\'>\n               postgresql\n           </a>\n     </li>\n     <li>\n       Run the following in terminal (Learn about pip\n       <a href=\'http://www.pythonforbeginners.com/pip/\' target=\'_blank\'>here</a>):\n     </li>\n   </ul>\n   <figure>\n     <pre>\n          <code class=\'language-python\' contenteditable spellcheck=\'false\' >pip install pipenv</code>\n          </pre>\n   </figure>\n </p>\n\n <h2 class=\'small_margin\'>Download Heroku tools</h2>\n <p> The tools can be found\n   <a href=\'https://devcenter.heroku.com/articles/getting-started-with-python#set-up\'\n     target=\'_blank\'> here</a>.\n     Download the appropriate package for your machine (i.e., Windows, Mac, etc.)\n </p>\n <p>Once downloaded, login to your heroku account in terminal. </p>\n\n <figure>\n  <pre>\n  <code class=\'language-python\' contenteditable spellcheck=\'false\' >heroku login</code>\n  </pre>\n  </figure>\n\n  <p>The following prompt should appear.</p>\n\n  <figure>\n   <pre>\n   <code class=\'language-python line-numbers\' contenteditable spellcheck=\'false\' >Enter your Heroku credentials:\nEmail: myemail@domain.com\nPassword: ********** </code>\n   </pre>\n   </figure>\n\n   <h2 class=\'small_margin\'>Install Heroku to the Project</h2>\n   <p>Once you have git installed in your project, you can create a Heroku app.</p>\n   <figure>\n  <pre>\n  <code class=\'language-python\' contenteditable spellcheck=\'false\' >heroku create myNewApp</code>\n  </pre>\n  </figure>\n  <p>In this case I named my app \'myNewApp\'. If no name is indicated, Heroku\n  automatically assigns a random name.</p>\n\n  <h2>Define a Procfile</h2>\n  <p>The\n    <a href=\'https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile\'\n    target=\'_blank\'>Procfile</a>\n     declares what command should be run to start your app. It\'s an empty text file\n     we create (with no extention) in the root of our project. It has one line of code.\n   </p>\n   <figure>\n       <pre>\n       <code class=\'language-python\' contenteditable spellcheck=\'false\' >web: gunicorn myProjectName.wsgi --log-file -</code>\n       </pre>\n       </figure>\n   <p>\n     Be sure to update it to your project name. In this case, my Django project\n     is called \'myProjectName\'.\n   </p>\n\n\n   <h2>Define a Pipfile</h2>\n   <p>\n     This step is crucial. A Pipfile is used by Heroku to pip install all the\n     necessary packages onto the Heroku server so that your app can run online\n     as well as it does locally. We create this file in the root of the project as\n     a text file (with no extension). Here is an example of what should be included\n     in the Pipfile.\n   </p>\n   <figure>\n       <pre>\n       <code class=\'language-python line-numbers\' contenteditable spellcheck=\'false\'>\n       [[source]]\n\n       url = \\"https://pypi.python.org/simple\\"\n       verify_ssl = true\n\n\n       [packages]\n\n       django = \\"*\\"\n       dj-database-url = \\"*\\"\n       psycopg2 = \\"*\\"\n       gunicorn = \\"*\\"\n       whitenoise = \\"*\\"\n       django-mako-plus = \\"*\\"\n\n\n\n\n       [requires]\n\n       python_version = \\"3.6\\"\n</code>\n       </pre>\n       </figure>\n       <p>An explanation of critical packages:</p>\n       <p class=\'p_indent\'>django, dj-database-url, psycopg2 - these are standard packages in Django.</p>\n       <p class=\'p_indent\'>\n         <a href=\'http://gunicorn.org\' target=\'_blank\'>gunicorn</a> -\n         This helps integrate Django projects into a web server.\n       </p>\n       <p class=\'p_indent\'>\n         <a href=\'http://whitenoise.evans.io/en/stable/\' target=\'_blank\'>whitenoise</a> -\n         This helps translate static link work in the Heroku server folder.\n       </p>\n       <p class=\'p_indent\'>\n         django-mako-plus - The custom framework package.\n       </p>\n       <p>\n         It\'s important to note that the \'*\' indicates the most current update of\n         that package. This can be hardcorded to a specific update (e.g., \\"3.2\\").\n       </p>\n\n       <h2>How to View Your Current Packages in Your Project</h2>\n       <p>\n          This command in the termnial displays all the packages currently installed\n          in your environment.\n       </p>\n       <figure>\n           <pre>\n           <code class=\'language-python\' contenteditable spellcheck=\'false\' >pip freeze</code>\n           </pre>\n       </figure>\n       <p>\n         This outputs the packages into a text file.\n       </p>\n       <figure>\n           <pre>\n           <code class=\'language-python\' contenteditable spellcheck=\'false\' >pip freeze > myTextFile.txt</code>\n           </pre>\n       </figure>\n\n       <h2 class=\'small_margin\'>Create Pipfile.lock</h2>\n       Once the Pipfile is created correctly, run the following in the terminal:\n       <figure>\n           <pre>\n           <code class=\'language-python\' contenteditable spellcheck=\'false\' >pipenv lock</code>\n           </pre>\n       </figure>\n       <p class=\'note\'>NOTE: you may need deactivate your virtual environment first.</p>\n\n       <h2>Change settings.py</h2>\n       <p>Update allowed hosts to the following. In this case, my domain name is\n       myWebsiteDomain.com.</p>\n       <figure>\n           <pre>\n           <code class=\'language-python\' contenteditable spellcheck=\'false\' >ALLOWED_HOSTS = [\'myWebsiteDomain.com\']</code>\n           </pre>\n       </figure>\n       <p>This allows any web server to access your project.</p>\n      <figure>\n        <pre>\n        <code class=\'language-python\' contenteditable spellcheck=\'false\' >ALLOWED_HOSTS = [\'*\']</code>\n        </pre>\n      </figure>\n      <p>Include whitenoise in the middleware.</p>\n      <figure>\n        <pre>\n        <code class=\'language-python line-numbers\' contenteditable spellcheck=\'false\' >MIDDLEWARE = [\n    . . .\n    \'whitenoise.middleware.WhiteNoiseMiddleware\',\n  ]</code></pre>\n      </figure>\n\n      <h2>Ready to Deploy? Me too.</h2>\n      <figure>\n        <pre>\n        <code class=\'language-python\' contenteditable spellcheck=\'false\' >git push heroku master</code>\n        </pre>\n      </figure>\n      <p class=\'note\'>\n        NOTE: Be sure you\'ve committed all of your changes. Also be sure you\'re committing\n        on master.\n      </p>\n\n      <h2>Create a PostgreSQL Database</h2>\n      <p>\n        Create a free PostgreSQL database on Heroku\'s server.\n      </p>\n      <figure>\n          <pre>\n          <code class=\'language-python\' contenteditable spellcheck=\'false\' >heroku addons</code>\n          </pre>\n      </figure>\n      <p>\n        Check the status of your database.\n      </p>\n      <figure>\n          <pre>\n          <code class=\'language-python\' contenteditable spellcheck=\'false\' >heroku pg</code>\n          </pre>\n      </figure>\n\n      <h2 class=\'small_margin\'>Update settings.py for the Database</h2>\n      <p>This should be included right after the database definition.\n        It\'s important to note that it\'s not necessary to remove your database\n        definition. Commit this and push it to the Heroku server.\n      </p>\n      <figure>\n          <pre>\n          <code class=\'language-python line-numbers\' contenteditable spellcheck=\'false\' >import dj_database_url\ndb_from_env = dj_database_url.config()\nDATABASES[\'default\'].update(db_from_env)</code>\n          </pre>\n    </figure>\n\n    <h2 class=\'small_margin\'>Run Database Migrations on Heroku</h2>\n    <figure>\n  <pre>\n  <code class=\'language-python line-numbers\' contenteditable spellcheck=\'false\' >heroku run python manage.py makemigrations # Including the app name is optional\nheroku run python manage.py migrate </code>\n  </pre>\n</figure>\n</div>\n\n<h2 class=\'small_margin\'>Done.</h2>\n<figure>\n  <pre>\n  <code class=\'language-python\' contenteditable spellcheck=\'false\' >heroku open</code>\n  </pre>\n</figure>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/duck_code/duck_code/home/templates/article.html", "uri": "article.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 5, "49": 263, "55": 2, "63": 2, "64": 3, "65": 3, "66": 3, "67": 3, "68": 3, "74": 6, "81": 6, "82": 7, "83": 7, "84": 9, "85": 9, "86": 10, "87": 10, "93": 87}}
__M_END_METADATA
"""
