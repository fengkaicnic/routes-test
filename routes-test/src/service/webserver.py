import webob.dec
import webob.exc
from src.config.router import MyRouter

def main():
    router = MyRouter()
    result = webob.Request.blank('/test').get_response(router)
    print result
    
if __name__ == '__main__':
    main()