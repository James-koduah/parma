from blueprints.admin import admin
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@admin.route('/hospital_register', methods=['get', 'post'], strict_slashes=False)
def hospital_register():
    """Route to register a hospital into the database"""
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
        hospital_staff = control.evaluate('Hospital_staff')
        hospital = control.make_query('Hospital', 'public_id', public_id)
        
        hospital_staff.update(user_id=user.id, hospital_id=hospital.id, public_id=f"{hospital.id}{user.id}")
        control.add_item(hospital_staff)
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
    confirm_invites = control.get_staff_invite_hospital(hospital.public_id, 'admin_confirm')
    pending_invites = control.get_staff_invite_hospital(hospital.public_id, 'pending')
    return render_template('admin/dashboard/dashboard.html', user=user, hospital=hospital, confirm_invites=confirm_invites, pending_invites=pending_invites)

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
    if user.username == invite_username:
        return jsonify({"response": "You can't send Yourself an invite"})
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
    """check if user is already a staff member"""
    user_is_staff = control.make_query("Hospital_staff", "public_id", f"{hospital.id}{invite_user.id}")
    if user_is_staff:
        return jsonify({"response": "User is already a staff member"})
    staff_invite = control.evaluate('Invite_staff')
    staff_invite.update(
            public_id=public_id,
            role=role,
            description=description,
            user_id=invite_user.public_id,
            user_name=invite_user.name,
            hospital_id=hospital.public_id,
            hospital_name=hospital.name,
            status='pending'
            )
    control.add_item(staff_invite)
    control.commit_session()
    return jsonify({"response": "success"})

@admin.route('/confirm_staff_invite/', methods=['post'], strict_slashes=False)
def admin_confirm_invite():
    user = auth_user()
    if user == False:
        return redirect('/')
    message = request.get_json()
    invite_id = message['invite_id']
    invite = control.make_query('Invite_staff', 'public_id', invite_id)
    if invite == None:
        return jsonify({"response": "The invitation is not valid"})
    invite.update(status='confirmed')
    staff = control.make_query('User', 'public_id', invite.user_id)
    hospital = control.make_query('Hospital', 'public_id', invite.hospital_id)
    add_staff = control.evaluate('Hospital_staff')
    add_staff.update(user_id=staff.id, hospital_id=hospital.id, public_id=f'{hospital.id}{staff.id}', user_role=invite.role)
    control.add_item(add_staff)
    staff_not_exists = control.commit_session()
    if staff_not_exists:
        return jsonify({"response": "success"})
    else:
        invite.update(status='closed')
        return jsonify({"response": "Person is already a staff member"})


