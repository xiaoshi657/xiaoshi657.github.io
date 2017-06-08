def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/wechat8000", WechatHandler),
            (r"/qrcode", QrcodeHandler),
            (r"/wechat8000/profile", ProfileHandler),
            (r"/menu", MenuHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "template")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
