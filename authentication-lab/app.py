from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey" : "AIzaSyC0NViXXtREB-z8Tau5zl5KUnk0PgB6X4w",
  "authDomain": "segev-firebase.firebaseapp.com",
  "projectId": "segev-firebase",
  "storageBucket": "segev-firebase.appspot.com",
  "messagingSenderId": "114124760344",
  "appId": "1:114124760344:web:30a595ad1cbf744cd66a6d",
  "measurementId": "G-BPSS8WEH38",
  "databaseURL" : "https://segev-firebase-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
            return render_template("signin.html")
    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        username = request.form['username']
        bio = request.form['bio']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            uid = login_session['user']['localId']
            user = {"email":email,"fullname":fullname,"username":username,"bio":bio}
            users = db.child("user").child(uid).set(user)
            return redirect(url_for('signin'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        try:
            uid = login_session['user']['localId']
            tweet = {"title":title,"text":text,"uid":}
            tweets = db.child("user").child(uid).set(tweet)
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)