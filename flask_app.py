#/usr/bin/env python3

def auth_user():
    """ function to authenticate users to access parts of the app"""
    auth_token = request.cookies.get('auth_parma')
    user_cookie = request.cookies.get('user_parma')
    if user_cookie: # Check if cookie exists
        allow_user = control.auth_token(auth_token, user_cookie)
        return allow_user
    else: # if user_cookie dosen't exist
        return False

from flask import Flask, render_template, request, redirect, jsonify, make_response
from flask_cors import CORS
from mysql_engine.control_orm import control
app = Flask(__name__)
CORS(app)
from sections.hospital import hospital

app.register_blueprint(hospital)



@app.route('/')
def welcome():
    return render_template('welcome/welcome.html')

@app.route('/app_package', strict_slashes=False)
def app_package():
    allow = auth_user()
    if allow == False:
        print('kkks')
        return redirect('/')
    username = request.cookies.get('user_parma')
    user = control.make_query('User', 'username', username)
    return render_template('app_package/app_package.html', user=user)

@app.route('/signup/', methods=['get', 'post'], strict_slashes=False)
def signup():
    firstname = request.form.get('first_name').capitalize()
    lastname = request.form.get('last_name').capitalize()
    name = f'{firstname} {lastname}'
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    """Check if username already exists"""
    check = control.make_query('User', 'username', username)
    if check:
        return render_template('error.html', message='Username Already in use')

    """Check if email already exists"""
    check = control.make_query('User', 'email', email)
    if check:
        return render_template('error.html', message='Email Already in use')

    """Make a unique public id"""
    while True:
        public_id = control.create_token(20) # random token 20 characters long alphanumeric
        check = control.make_query('User', 'public_id', public_id)
        if check == None:
            break
    """Add user to database"""
    user = control.evaluate('User')
    login_token = control.create_token(20)
    user.update(
            name=name,
            username=username,
            email=email,
            password=password,
            public_id=public_id,
            login_token=login_token,
            )
    control.add_item(user)
    control.commit_session()
    response = make_response(redirect('/app_package'))
    response.set_cookie('auth_parma', f'{user.login_token}')
    response.set_cookie('user_parma', f'{user.username}')
    return response

@app.route('/login', methods=['get', 'post'], strict_slashes=False)
def login():
    if request.method == 'POST':
        """Get Credentials"""
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        """If the user is logging in with username"""
        if username != '':
            user = control.make_query('User', 'username', username)
            if user == None or user.password != password:
                return render_template('error.html', message='Wrong Username')

        """if the user is logging in with email"""
        if email != '':
            user = control.make_query('User', 'email', email)
            if user == None or user.password != password:
                return render_template('error.html', message='Wrong email')

        response = make_response(redirect(f'/app_package'))#change redirect to approiate route
        response.set_cookie('auth_parma', f'{user.login_token}')
        response.set_cookie('user_parma', f'{user.username}')
        return response
    return render_template('login/login.html')

if __name__ == '__main__':
    control.start_session()
    app.run(host='0.0.0.0', port=5000)

