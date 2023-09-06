from blueprints.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@hospital.route('/<hospital_id>', strict_slashes=False)
def hospital_main(hospital_id):
    user = auth_user()
    if user == False:
        return redirect('/')
    hospital = control.make_query('Hospital', 'public_id', hospital_id)
    is_admin = control.check_admin_status(hospital_id, user.public_id)
    if is_admin:
        return redirect(f'/admin/dashboard/{hospital.public_id}')
    else:
        return redirect(f'/hospital/{hospital_id}/{user.public_id}')


@hospital.route('/<hospital_id>/<user_id>', strict_slashes=False)
def hospital_work(hospital_id, user_id):
    user = auth_user()
    if user == False:
        return redirect('/')
    if user.public_id != user_id:
        return render_template('basic/error.html', message='You are not Authorized to veiw this page')
    staff = control.make_query('User', 'public_id', user_id)
    hospital = control.make_query('Hospital', 'public_id', hospital_id)
    is_staff = control.make_query('Hospital_staff', 'public_id', f'{hospital.id}{staff.id}')
    if is_staff == None:
        return render_template('basic/error.html', message='You are not a staff of this hospital')
    staff.role = is_staff.user_role
    if staff.role == 'Doctor':
        return render_template('hospital/staff/doctor.html', user=staff, hospital=hospital, appointments=['a', 'v'])
    if staff.role == 'Nurse':
        return render_template('hospital/staff/nurse.html', user=staff, hospital=hospital)
    return render_template('basic/error.html', message='Error, cannot process user data, notification sent to team')
