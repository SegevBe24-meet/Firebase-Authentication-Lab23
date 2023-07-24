from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    try:

    except:    
    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('signin'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

config = {
  "apiKey" : "AIzaSyC0NViXXtREB-z8Tau5zl5KUnk0PgB6X4w",
  "authDomain": "segev-firebase.firebaseapp.com",
  "projectId": "segev-firebase",
  "storageBucket": "segev-firebase.appspot.com",
  "messagingSenderId": "114124760344",
  "appId": "1:114124760344:web:30a595ad1cbf744cd66a6d",
  "measurementId": "G-BPSS8WEH38",
  "databaseURL" : ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


if __name__ == '__main__':
    app.run(debug=True)