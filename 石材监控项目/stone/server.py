#encoding=utf-8

## Copyright (C), 2013-2014, ****.
## File name:       server.py
## Author:          tancj    30778121@qq.com
## Version:         0.1.7
## Date:            2014-09-10
## Description:     The KCSS(Keda Cloud Storage System) server realize the base function "showing different informations (Errors/Warnings/Informations/Other...) of the logs, and the config.conf gives the address of logs"
## Others:          none
## History:         none 
##   1. Date:
##      Author: 
##      Modification:
##   2. ...

import sys
import getopt
import MySQLdb
import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import setting
#from setting import urls
#from setting import PORT
#from setting import SETTINGS
#from setting import myCookeSecret
#from setting import *

def argv_get():
    '''
    server.py 
    Usage:run a website to modify password for SVN, before run, you should 
    configure passwd.conf correctly
    -P port 
    -h help file
    --port port
    --help help file
    python server.py -P 8888 or python server.py --port 8888
    '''
    try:
        opts,args = getopt.getopt(sys.argv[1:], "hP:", ["help","port="])
    except:
        print "argv read error"
        print argv_get.__doc__
        sys.exit()
    for option,parameter in opts:
        if option in ("-h","--help"):
            print argv_get.__doc__
            sys.exit()
        elif option in ("-P","--port"):
#            global PORT
            setting.PORT = parameter 
            return 0


	
        
def main():
    #tornado.options.parse_command_line()
    application = tornado.web.Application(
                    handlers = setting.urls,
                    cookie_secret=setting.myCookeSecret,
                    debug = True,
                    **setting.SETTINGS
                    )

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(setting.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    argv_get()
    main()

