class decorator(object):
    def __init__(self, fn):
        print 'decorator'
        self.fn = fn
        print self.fn
        
    def __call__(self, fn):
        print fn
        def serve(*args):
            print args
            return fn(*args)
        print '__call'
        return serve

@decorator(123)
def quare(a, b):
    print a**2
    return 'have lhxctfws'
    
print (quare(2, 1))   