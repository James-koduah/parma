from blueprints.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@hospital.route('/<hospital_id>/invite/<invite_id>', methods=['get', 'post'], strict_slashes=False)
def hospital_invite(hospital_id, invite_id):
    user = auth_user()
    if user == False:
        return redirect('/login')

    invite = control.make_query('Invite_staff', 'public_id', invite_id)
    if invite == None or invite.status != 'pending': # If something has happended and the invite is no longer valid
        return render_template('basic/error.html', message='This invite is no longer valid')
    hospital = control.make_query('Hospital', 'public_id', hospital_id)
    if hospital == None: # If something has happende and this hospital no longer exists
        return render_template('basic/error.html', message='This invite is no longer valid')

    if request.method == 'POST':
        return "form"
    return render_template('hospital/invite/invite.html', user=user, invite=invite)

@hospital.route('/accept_invite/<invite_id>', methods=['post'], strict_slashes=False)
def hospital_invitee_accept_invite(invite_id):
    user = auth_user()
    if user == False:
        return redirect('/login')
    #TODO: Accept the approitate information and other things
    invite = control.make_query('Invite_staff', 'public_id', invite_id)
    if invite:
        invite.update(status='admin_confirm')
        control.commit_session()
    else:
        return render_template('basic/error.html', message='This invite is no longer valid')
    return redirect(f'/user/{user.username}')
