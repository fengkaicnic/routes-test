class decorator(object):
    
    abc = 35
    def __init__(self, abc=None):
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
        

class Tone(object):

    @decorator(123)
    def quare(self, a, b):
        print a**2
        return 'have lhxctfws'
    
    @decorator(235)
    def __call__(self, a, b):
        print 'this is call'
        return a**2
    
one = Tone()  
print '2222222222222222'
print one.quare(1, 2)
print '3333333333333333'
print one(2, 1)