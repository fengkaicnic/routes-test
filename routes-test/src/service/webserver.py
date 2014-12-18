import webob.dec
import webob.exc
from src.config.router import MyRouter

def main():
    router = MyRouter()
    keys = raw_input()
    
    if keys == 'test':
        result = webob.Request.blank('/test').get_response(router)
    if keys == 'test1':
        result = webob.Request.blank('/test1').get_response(router)
    print result
    
if __name__ == '__main__':
    main()