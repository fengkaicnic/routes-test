
class TestController(object):
    def getlist(self, mykey):
        print 'getlist is invoked'
        return 'getlist(), %s' % mykey

class Application(object):
    
    def __init__(self, controller):
        self._controller = controller
    
    def __call__(self, environ, start_response):
        print 'Application is invoked'
        action_args = environ['wsgiorg.routing_args'][1].copy()
        try:
            del action_args['controller']
        except KeyError:
            pass
        
        try:
            del action_args['format']
        except KeyError:
            pass
        
        action = action_args.pop('action', None)
        controller_method = getattr(self._controller, action)
        result = controller_method(**action_args)
        
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [result]
        

        