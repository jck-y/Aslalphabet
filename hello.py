from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if 'myFile' not in request.files:
        return 'No file uploaded', 400

    file = request.files['myFile']

    if file.filename == '':
        return 'No file selected', 400

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Get the URL of the uploaded file
    uploaded_file_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    return f'File uploaded successfully. URL: {uploaded_file_url}'

if __name__ == "__main__":
    app.run()
