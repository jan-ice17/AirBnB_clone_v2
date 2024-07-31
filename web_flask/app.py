#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return "This is my about page"

if __name__ == '__main__':
    app.run(debug=True) #by default runs on port http://127.0.0.1.5000/
