from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
active_users = []
registr_users={}
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
    data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials", 'users': users, 'isloggedin': True}
    return render_template('index_data.html', data=data)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        if name not in registr_users.keys():
            registr_users[name] = password
            active_users.append(name)
        elif name in registr_users.keys() and name not in active_users:
            if password != registr_users[name]:
                return f'wrong password'
            else:
                return f'{name} has logged'
        else:
            active_users.remove(name)
            return f'{name} has been logged out'
        return f'{name} has logged'
    else:
        return render_template('login.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0')