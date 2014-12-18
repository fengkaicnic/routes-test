from routes import Mapper
import webob.dec
import webob.exc
import routes.middleware
from src.controller.controller import TestController
from src.controller.controller import Application

class MyRouter(object):
    
    def __init__(self):
        route_name = 'test_route'
        route_path = '/test'
        
        my_application = Application(TestController())
        
        self.mapper = Mapper()
        self.mapper.connect(route_name, route_path,
                            controller=my_application,
                            action='getlist',
                            conditions={'method':['GET']})
        
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)
    @webob.dec.wsgify(RequestClass=webob.Request)  
    def __call__(self, req):
        
        print 'MyRouter is invoked'
        return self._router

    @staticmethod
    @webob.dec.wsgify(RequestClass=webob.Request)
    def _dispatch(self, req):
        print 'RoutesMiddleware is invoked, calling the dispatch back'
        match_dict = req.environ['wsgiorg.routing_args'][1]
        if not match_dict:
            return webob.exc.HTTPNotFound()
        app = match_dict['controller']
        return app

#class RoutingTestCase(testtools.TestCase):
    
#    def test_router(self):
#        router = MyRouter()
#        result = webob.Request.blank('/test').get_response(router)
#        self.assertEqual(result.body, "getlist(), mykey=myvalue")
        
    