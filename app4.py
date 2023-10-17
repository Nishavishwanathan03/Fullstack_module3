from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)


# CREATE A COOKIE
@app.route('/')
def index():
        cookie = make_response("Creating a cookie")
        cookie.set_cookie('name', 'Suresh', max_age=60*60)
        return (cookie)

# READ THE COOKIE
@app.route('/read')
def read_cookie():
        if request.cookies.get('name'):
               cookie = make_response("Display Cookie : {}".format(request.cookies.get('name')))
        else:
               cookie = make_response("Creating a Cookie")
               cookie.set_coookie('name','priya',max_age = 60*60)
               return (cookie)
               

        if __name__ == '__main__':
            app.run(debug=Trye, port=5000)