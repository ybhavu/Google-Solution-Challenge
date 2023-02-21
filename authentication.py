import pyrebase

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

email = 'test@gmail.com'
password  = '123456'

# How to create new User
# ID Token important
# user  = auth.create_user_with_email_and_password(email,password)
# print(user)

user = auth.sign_in_with_email_and_password(email,password)
# info = auth.get_account_info(user['idToken'])
# print(info)

# #email Verifiaction
# auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)
