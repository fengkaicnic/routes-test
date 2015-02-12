class decorator(object):
    
    abc = 35
    def __init__(self, bcd, abc=None):
        print 'decorator'
        self.abc = abc
#        print fn1
        print self.abc
        
    def __call__(self, *args):
        self.fn = args[0]
        def serve(*args):
            print args
            return self.fn(*args)
        print '__call'
        return serve
    
    def __get__(self, obj, owner):
        print 'in get', obj, owner
        

@decorator(123)
def quare(a, b):
    print a**2
    return 'have lhxctfws'
    
print (quare(2, 1))   