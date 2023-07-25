from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyCXR-P0Y7zDqrwh1ZjE1jNQP7mmTGhjBks",
  "authDomain": "yasmina-8924e.firebaseapp.com",
  "projectId": "yasmina-8924e",
  "storageBucket": "yasmina-8924e.appspot.com",
  "messagingSenderId": "119957533832",
  "appId": "1:119957533832:web:4c83d74542d91309fd1b3d",
  "measurementId": "G-QC2BFH39R5",
  "databaseURL": "https://yasmina-8924e-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db= firebase.database()

app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
     

        except:
            error = "Authentication failed"

    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        username = request.form['username']
        bio = request.form['bio']
       

        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"email" : email , "password" : password , "username" : username , "name"  : name , "bio" : bio}
            UID = login_session['user']['localId']
            db.child("Users").child(UID).set(user)
            users = db.child("Users").get().val()
            return redirect(url_for('add_tweet'))
        except:
            error = "Authetication faild"
    return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        UID = login_session['user']['localId']
        tweet = {"uid" : UID , "title" : title , "text" : text}
        db.child("Tweets").push(tweet)
    return render_template("add_tweet.html")

@app.route('/all_tweets')
def all_tweets():
    tweets = db.child("Tweets").get().val()
    return render_template("tweets.html" , tweets = tweets)




if __name__ == '__main__':
    app.run(debug=True)