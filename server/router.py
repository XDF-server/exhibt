# *-* coding:utf-8 *-* 

import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

import loader
from gl import LOG
from api_handler import *
from exhibt_handler import *

define('port',default = 9000,help='this is default port',type = int)

if __name__ == "__main__":
		
	tornado.options.parse_command_line()

	application = tornado.web.Application([
		(r"/test", TestHandler),
		(r'/transcode',Transcode),
		(r'/transcode_res',TranscodeRes),
		(r'/upload_question',UploadQuestion),
		(r'/uptoken',Uptoken),
		(r'/index',Index),
		(r'/search',Search),
	],
	template_path = os.path.join(os.path.dirname(__file__),os.pardir,'templates'),
	static_path = os.path.join(os.path.dirname(__file__),os.pardir,'static'),
	)

	http_server = tornado.httpserver.HTTPServer(application)

        http_server.listen(options.port)

	LOG.info('idc_api is started,port is [%s]' % options.port)

        tornado.ioloop.IOLoop.instance().start()
