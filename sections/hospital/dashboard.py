from sections.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@hospital.route('/dashboard/', strict_slashes=False)
def hospital_dashboard():
    return render_template('hospital/dashboard/dashboard.html')

@hospital.route('/register', methods=['get', 'post'], strict_slashes=False)
def hospital_register():
    allow = auth_user()
    if allow == False:
        return redirect('/')

    if request.method == 'POST':
        name = request.form.get('name')
        country = request.form.get('country')
        address = request.form.get('address')
        """generate public_id"""
        while True:
            public_id = control.create_token(20)
            check = control.make_query('Hospital', 'public_id', public_id)
            if check == None:
                break

        new_hospital = control.evaluate('Hospital')
        new_hospital.update(
                public_id=public_id,
                name=name,
                country=country,
                address=address
                )
        control.add_item(new_hospital)
        control.commit_session()
        return redirect('/hospital/dashboard')
    username = request.cookies.get('user_parma')
    user = control.make_query('User', 'username', username)
    return render_template('hospital/register/register.html', user=user)
    #return "Hello World"
"""
@hospital.route('/<public_id>', methods='get strict_slashes=False)
def hospital(public_id):
    control.start_session()
    hospital = control.make_query('Hospital', 'public_id', public_id)
    return render_template('hospital/hospital.html', hospital=hospital)

@hospital.route('/staff_register/<public_id>', methods=['get', 'post'], strict_slashes=False)
def staff_register(public_id):
    control.start_session()
    hospital = control.make_query('Hospital', 'public_id', public_id)
    if request.method == 'POST':
        return render_template(
                'confirmation.html',
                header='Thank You',
                content='Your submission has been sent to your admin for confirmation',
                action='You will be redirected in a few seconds'
                )
    return render_template('hospital/staff_register.html', hospital=hospital)
"""
