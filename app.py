import flask
from flask import Flask,session,render_template,request,redirect
import pyrebase

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyAcICpBE-tRkISB6ZBZi0HSeFdITwn48m4",
    'authDomain': "project1-fe081.firebaseapp.com",
    'projectId': "project1-fe081",
    'storageBucket': "project1-fe081.appspot.com",
    'messagingSenderId': "65876192735",
    'appId': "1:65876192735:web:93a49c2331dcbf95aee86a",
    'measurementId': "G-H94FXZ87W4",
    'databaseURL': ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key= 'secret'

@app.route('/', methods=['POST','GET'])
def index():
    if('user' in session):
        return 'Hi,{}'.format(session['user'])
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        try:
           user = auth.sign_in_with_email_and_password(email,password)
           session['user']=email
        except:
            return 'Failed to Login'

    return render_template('index.html')

@app.route('/logout')
def logout():
    # pass
    session.pop('user')
    return redirect('/')

if __name__=='__main__':
    app.run(port = 5501)