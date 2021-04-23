from flask import Flask, session, render_template, request, redirect, Markup
from counter import count_words
from werkzeug.utils import secure_filename
import os
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/word_count', methods=['POST'])
def word_count():
    filename = request.files['doc']
    filename.save(secure_filename(filename.filename))
    words = count_words(filename)
    files = glob.glob('*.docx')
    for i in files:
        try:
            os.remove(i)
        except:
            pass
    return render_template('index.html', words=words)

if __name__ == '__main__':
    app.run(debug=True)