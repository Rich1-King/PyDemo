# -*- coding: UTF-8 -*-
from web import get

@get('hello')
def sayHello():
    return 'hello'


