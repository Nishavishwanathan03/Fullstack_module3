from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return("this is the Nisha's flask application")

@app.route('/about')
def about():
    return("this is the Nisha's flask application")


if __name__== '__main__':
  app.run(debug = True, port=5000)