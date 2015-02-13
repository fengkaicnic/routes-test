from routes import Mapper
import webob.dec
import webob.exc
import routes.middleware
from src.controller.controller import TestAction 
from src.controller.controller import Application

class MyResourceRouter(object):
    
    def __init__(self):
        route_name = 'resource'
        route_path = 'resor'
        
        my_application = Application(TestAction())
        
        self.mapper = Mapper()
        self.mapper.resource(route_name, route_path, controller=my_application)
        
        self.mapper.connect('resconnct', '/getkey',
                            controller=my_application,
                            action='getkey',
                            conditions={'method':['GET']})
        
        self._router = routes.middleware.RoutesMiddleware(self._dispatch, self.mapper)
        
    @webob.dec.wsgify(RequestClass=webob.Request)  
    def __call__(self, req):
        
        print 'MyRouter is invoked'
        return self._router

    @staticmethod
    @webob.dec.wsgify(RequestClass=webob.Request)
    def _dispatch(req):
        print 'RoutesMiddleware is invoked, calling the dispatch back'
        match_dict = req.environ['wsgiorg.routing_args'][1]
        if not match_dict:
            return webob.exc.HTTPNotFound()
        app = match_dict['controller']
        return app

class MyRouter(object):
    
    def __init__(self):
        route_name = 'test_route'
        route_path = '/test'
        self.count = 1
        
        my_application = Application(TestAction())
        
        self.mapper = Mapper()
        self.mapper.connect(route_name, route_path,
                            controller=my_application,
                            action='getlist',
                            conditions={'method':['GET']})
        
        self.mapper.connect(route_name, '/test1',
                            controller=my_application,
                            action='getkey',
                            conditions={'method':['GET']})
        
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)
    @webob.dec.wsgify(RequestClass=webob.Request)  
    def __call__(self, req):
        
        print 'MyRouter is invoked'
        return self._router

    @staticmethod
    @webob.dec.wsgify(RequestClass=webob.Request)
    def _dispatch(req):
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
        
    