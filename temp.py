import pyrebase

firebaseconfig = {
    'apiKey': "AIzaSyCe3AOYttBOSqy3WJU3tsYpcwYy4r6j_0s",
    'authDomain': "pushgram-mobile.firebaseapp.com",
    'projectId': "pushgram-mobile",
    'storageBucket': "pushgram-mobile.appspot.com",
    'messagingSenderId': "605706942308",
    'appId': "1:605706942308:web:80385154abe5fb64882c71",
    'measurementId': "G-LBXDNVD3T3",
    "databaseURL": "https://pushgram-mobile-default-rtdb.firebaseio.com/"
}
fbase = pyrebase.initialize_app(firebaseconfig)
auth = fbase.auth()

def signup():
    email=input("email: ")
    password = input("Password: ")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print("Sign up completed")
    except:
        print("Email already exist")
def Login():
    email = input("email: ")
    password = input("password: ")
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        print("sign in completed")
        
    except:
        print("Wrong email or password")
        
if __name__ == "__main__":
    print("[1]: Sign up\n[2]: Sign in")
    option = int(input())
    if option == 1:
        signup()
    elif option == 2:
        Login()