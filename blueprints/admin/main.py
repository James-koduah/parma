from blueprints.admin import admin
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@admin.route('/hospital_register', methods=['get', 'post'], strict_slashes=False)
def hospital_register():
    user = auth_user()
    if user == False:
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
        """We give whoever is creating this hospital admin status"""
        admin = control.evaluate('Admin')
        admin.update(user_id=user.public_id, hospital_id=public_id)
        control.add_item(admin)
        control.add_item(new_hospital)
        control.commit_session()
        """Add the user to the hospital.
           We can only get the hospital id after we have commited to the database
        """
        user_hospital = control.evaluate('Hospital_User')
        hospital = control.make_query('Hospital', 'public_id', public_id)
        user_hospital.update(user_id=user.id, hospital_id=hospital.id)
        control.add_item(user_hospital)
        control.commit_session()
        return redirect(f'/admin/dashboard/{public_id}')

    return render_template('admin/hospital_register/register.html', user=user)


@admin.route('/dashboard/<hospital_id>', strict_slashes=False)
def admin_dashboard(hospital_id):
    user = auth_user()
    if user == False:
        return redirect('/')
    is_admin = control.check_admin_status(hospital_id, user.public_id)
    if is_admin == None:
        return render_template('basic/error.html', message='You are not Authorized')
    hospital = control.make_query('Hospital', 'public_id', hospital_id)
    return render_template('admin/dashboard/dashboard.html', user=user, hospital=hospital)

@admin.route('/invite_staff/', methods=['post'], strict_slashes=False)
def admin_invite_staff():
    user = auth_user()
    if user == False:
        return redirect('/')
    message = request.get_json()
    role = message['role']
    description = message['job_description']
    invite_username = message['invite_username']
    hospital_id = message['hospital_id']
    """generate public_id"""
    while True:
        public_id = control.create_token(20)
        check = control.make_query('Invite_staff', 'public_id', public_id)
        if check == None:
            break
    """Get user from database"""
    invite_user = control.make_query('User', 'username', invite_username)
    if invite_user == None:
        return jsonify({"response": "Error, Wrong Username"})
    """Get Hospital from database"""
    hospital = control.make_query("Hospital", 'public_id', hospital_id)
    staff_invite = control.evaluate('Invite_staff')
    staff_invite.update(
            public_id=public_id,
            role=role,
            description=description,
            user_id=invite_user.public_id,
            hospital_id=hospital.public_id,
            status='pending'
            )
    control.add_item(staff_invite)
    control.commit_session()
    return jsonify({"response": "success"})


