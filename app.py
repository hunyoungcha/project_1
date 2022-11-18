


from flask import Flask, render_template, request, session, url_for, redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 
