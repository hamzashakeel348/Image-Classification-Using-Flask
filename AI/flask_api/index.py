
from flask import Flask, render_template, request, redirect, flash
import main
import urllib.request
from app import app
from werkzeug.utils import secure_filename
from main import getLabels, initialize
import os


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_file():
    initialize()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            label = getLabels(filename)
            flash(label)
            flash(filename)
            return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
