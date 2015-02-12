class decorator(object):
    
    abc = 35
    def __init__(self, func=None, abc=None):
        print 'decorator'
        self.abc = abc
        self.fn = func
#        print fn1
        print self.abc
        
    def __call__(self, *args):
        print self.fn
        def serve(*args):
            print args
            return self.fn(*args)
        print '__call'
        return serve

@decorator(abc=123)
def quare(a, b):
    print a**2
    return 'have lhxctfws'
    
print (quare(2, 1))   