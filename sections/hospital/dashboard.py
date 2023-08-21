from sections.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user



@hospital.route('/register', methods=['get', 'post'], strict_slashes=False)
def hospital_register():
    allow = auth_user()
    if allow == False:
        return redirect('/')
    username = request.get.cookies('user_parma')
    user = request.
    return render_template('hospital/register/main.html', user=)
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
