from tornado.web import (RequestHandler,
                         Application,
                         url
                         )

class MainHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")

urls = [url(r"/app", MainHandler),
        url(r"/", MainHandler)]

application = Application(urls)

if __name__ == "__main__":
    application.listen(8888)

    import tornado.ioloop
    tornado.ioloop.IOLoop().current().start()