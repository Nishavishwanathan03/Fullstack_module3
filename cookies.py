from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i_Love_india'


# CREATE A COOKIE
@app.route('/')
def index():
        if 'hits' in session:
               session['hits']= session.get('hits')+1
        else:
               session['hits'] = 1
               return("Total Number of Hits on the Application # {}". format(session.get('hits')))
        
# DESTROY A SESSION
@app.route('/delete')
def delete():
        session.pop('hits',None)
        return("session Deleted Successfully")
        
               

        if __name__ == '__main__':
            app.run(debug=Trye, port=5000)















