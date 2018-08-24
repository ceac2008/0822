import web
urls = (
    '/(.*)', 'hello'
)

class hello:
    def GET(self, name):
        if not name:
            name = 'world'
        print('Hello,', name + '!')
        return 'Hello, ' + name + '!'


    def post(self):
        return "post"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()