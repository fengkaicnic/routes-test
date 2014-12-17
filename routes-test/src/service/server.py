from wsgiref.simple_server import make_server
from src.controller.controller import TestController
from src.config.router import MyRouter

def main():
    httpd = make_server('', 9999, MyRouter())
    print 'serving on port 9999'
    
    httpd.server_forever()


if __name__ == '__main__':
    main()    