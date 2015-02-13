import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World.\n")
        
application = tornado.web.Application([(r'/', MainHandler), ])

if __name__ == '__main__':
    application.listen(8899)
    tornado.ioloop.IOLoop.instance().start()