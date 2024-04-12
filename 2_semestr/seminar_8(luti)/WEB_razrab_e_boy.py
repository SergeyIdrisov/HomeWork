from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h1 style='color:green'>Hello World!</h1>"
@app.route("/help")
def help():
    return "help me"
@app.route("/post/<id>")
def show_post(id):
    return "post id is " + id

@app.route("/bookmarks")
def display_bookmarks():
    bk = request.args.get("page", "1")
    return "the bookmark page is " + bk

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')