import  web
urls = (
    '/(.*)', 'hello',
    '/hello_1[/]?.*', 'hello_1',
    '/hello_2[/]?.*', 'hello_2',
    #'/hello_2/name=(.*)&age=(.*)', 'hello_2',
    '/hello_3[/]?.*','hello_3',
    '/hello_4[/]?.*','hello_4',
    '/hello_5[/]?.*','hello_5',
    '/delete[/]?.*','delete',
    '/toupdate[/]?.*','toupdate',
    '/update[/]?.*','update',
)
db=web.database(dbn='mysql',db='test',user='root',
                 pw='root',charset='utf8',port=3306)
app = web.application(urls, globals())
render = web.template.render('templates')
class hello:
    def GET(self, name):
        if not name:
            name = 'world'
        print('Hello,', name + '!')
        return 'Hello, ' + name + '!'


    def post(self):
        return "post"
class hello_1:
    def GET(self):
        return render.index_1()

class hello_2:
    def GET(self):
        i = web.input(name='mike', age=18)
        print(i.name, i.age)
        # return render.index_2(i.name,i.age)
        '''也可以使用下面的'''
        render = web.template.frender("templates/index_2.html")
        return render(i.name, i.age)

class hello_3:
    def GET(self):
        render = web.template.frender("templates/index_3.html")
        return render()
class hello_4: #添加
    def POST(self):
        i = web.input(tc=[])
        db.insert('student',user=i.user,pwd=i.pwd,tc=",".join(i.tc))
        #return "Hello, form!"
        raise web.seeother("hello_5")
class hello_5: #查询
    def GET(self):
        results = db.select('student')
        render = web.template.frender("templates/index_4.html")
        # for r in results:
        #     print(r)
        return render(results)
class delete: #删除
    def GET(self):
        i=web.input(Id=None)
        print(i.Id)
        db.delete('student',where="Id=%d"%int(i.Id))
        raise web.seeother("hello_5")
class toupdate: #修改回显
    def GET(self):
        i=web.input(Id=None)
        print(i.Id)
        results=db.select('student',where="Id=%d"%int(i.Id))
        # for i in results:
        #     print(i)
        render = web.template.frender("templates/update.html")
        return render(results)
class update: #修改回显
    def POST(self):
        i = web.input(tc=[])
        db.update('student',where="Id=%d"%int(i.Id),user=i.user, pwd=i.pwd, tc=",".join(i.tc))
        # return "Hello, form!"
        raise web.seeother("hello_5")
if __name__ == "__main__":
    app.run()