from flask import render_template
from flask import url_for 
from flask import redirect
from flask import request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'C:\Users\Administrator\Documents\nisha'
app.config['SECRET_KEY'] = 'I_love_pizza'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@app.route('/',methods = ['GET','POST,'])
def index():
    if request.method == 'POST':
        file = request.file['file']
        if 'file' not in request.files:
            return redirect('/')
        elif (fie.filename == ''):
            return ("<script> alert('File Not Found !')</script")
        elif (file):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect('/')
        else:
            return redirect(request.url)
        return render_template('upload.html')

if __name__ == '__main__':
            app.run(debug=True, port=5000)