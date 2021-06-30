from flask import Flask

UPLOAD_FOLDER = '/home/hamza/Desktop/AI/flask_api/upload'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
