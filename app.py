from flask import Flask, session, render_template, request, redirect, Markup
from counter import count_words
from werkzeug.utils import secure_filename
import os
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', regex='\([^()]*\, ?[0-9]*\)')

@app.route('/word_count', methods=['POST'])
def word_count():
    regex = request.form['regex']
    filename = request.files['doc']
    try:
        filename.save(secure_filename(filename.filename))
    except FileNotFoundError:
        return render_template('index.html', words="Invalid file input", regex=regex)
    words = count_words(filename, regex)
    files = glob.glob('*.docx')
    for i in files:
        try:
            os.remove(i)
        except:
            pass
    return render_template('index.html', words=words, regex=regex)

if __name__ == '__main__':
    app.run(debug=True)