from wsgiref.simple_server import make_server
from src.controller.controller import TestAction
from src.config.router import MyRouter
import os

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello world!\n'

def main():
    httpd = make_server('', 9999, MyRouter())
    print 'serving on port 9999'
    
    httpd.serve_forever()


if __name__ == '__main__':
    main()     