from wsgiref.simple_server import make_server
from src.controller.controller import TestAction
from src.config.router import MyResourceRouter
import os

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello world!\n'

def main():
    httpd = make_server('', 9997, MyResourceRouter())
    print 'serving on port 9997'
    
    httpd.serve_forever()


if __name__ == '__main__':
    main()     