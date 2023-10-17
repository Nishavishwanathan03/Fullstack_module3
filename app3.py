from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods =['GET','POST'])
def index():
    if request.method == 'POST':
        form = request.form
        name = form['my_name']
        return render_template('display.html', data = name)
    return rebder_template('suman.html')
        

        if __name__ == '__main__':
            app.run(debug=Trye, port=5000)