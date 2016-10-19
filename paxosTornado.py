import tornado
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from paxosChallenge  import app
import tornado.options

tornado.options.parse_command_line() #Enables access.log 

http_server = HTTPServer(WSGIContainer(app), ssl_options={
        "certfile": "cert.pem",
        "keyfile": "key.pem",
})
http_server.listen(443)
IOLoop.instance().start()


