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
  "measurementId": "G-QC2BFH39R5"
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
            except:
                error = "Authentication failed"
    return render_template("signin.html")







@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
         try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
            except:
                error = "Authentication failed"
    return render_template("signin.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)