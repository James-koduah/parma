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
    return "Doctor or nursing page"
