# -*- coding: utf-8 -*-
from tornado.options import define, options
import tornado.ioloop
import tornado.web
from urls import *
    
application = tornado.web.Application(
    handlers = urls
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8881)
    tornado.ioloop.IOLoop.instance().start()
    
