
import bottle
from bottle import default_app, run, route, template, static_file, error, abort
application = bottle.default_app()
from sys import argv


frettir = [["NewsNewsNews", "Today on the new are some news about news but first, the news", "news.jpg", "news@reputable.com"],
           ["BREAKING NEWS", "There seems to be a surge in new news, so stay tuned for even more news", "breaking-news.jpg", "dave15@yahoo.com"],
           ["Fake news", "The recent surge in new new has been uncoverd as being FAKE NEWS. there are stikingly little news to go around", "fake-news.jpg", "reporterman@newnews.org"],
           ["No more news", "Yup... all out of news", "news-update.jpg", "news@reputable.com"]]

@route('/')
def index():
    return template('index.tpl',id=0)
@route('/<id:int>')
def new(id):
    return template("news.tpl", title=frettir[id-1][0], news=frettir[id-1][1], img = frettir[id-1][2], author=frettir[id-1][3])



@route('/static/<skra:path>')
def static_skra(skra):
    return static_file(skra, root='./public/')
#run(host='localhost', port=9000, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])
