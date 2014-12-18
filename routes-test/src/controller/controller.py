
class TestAction(object):
    def getlist(self, body, mykey):
        print 'getlist is invoked'
        return 'getlist(), %s \n' % body
    
    def getkey(self, mykey, body):
        print 'getkey is invoked'
        return 'getkey() %s \n' % mykey

class Application(object):
    
    def __init__(self, controller):
        self._controller = controller
    
    def __call__(self, environ, start_response):
        print 'Application is invoked'
        action_args = environ['wsgiorg.routing_args'][1].copy()
        querys = environ['QUERY_STRING']
        try:
            del action_args['controller']
        except KeyError:
            pass
        
        try:
            del action_args['format']
        except KeyError:
            pass
        
        action = action_args.pop('action', None)
        action_args['mykey'] = querys
        action_args['body'] = querys
        controller_method = getattr(self._controller, action)
        result = controller_method(**action_args)
        
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [result]
        

        