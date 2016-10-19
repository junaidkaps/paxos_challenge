import tornado
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from paxosChallenge  import app


http_server = HTTPServer(WSGIContainer(app), ssl_options={
        "certfile": "cert.pem",
        "keyfile": "key.pem",
})
http_server.listen(443)
IOLoop.instance().start()


