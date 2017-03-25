# -*- coding: UTF-8 -*-
import os
from web import WSGIApplication, Jinja2TemplateEngine
import Apis

wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
#template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
#wsgi.template_engine = template_engine

wsgi.add_module(Apis)

if __name__ == '__main__':
    wsgi.run(9000)