from blueprints.user import user
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@user.route('/<username>', strict_slashes=False)
def user_main(username):
    """This is the users homePage
       Like popular sites like twitter and linkedin where you can see the user's personal page
       If the user is viewing his/her own page, what they will see should be different from what the general public sees.
       We are rendering two different pages to the people who come to this page whether they are logged in or not
    """
    user = auth_user()
    page = control.make_query('User', 'username', username)
    if user: # If the user is the same veiwing his own page
        if page.username == user.username:
            staff_invites = control.get_staff_invite_user(user.public_id, 'pending')
            for hospital in user.hospitals:
                staff_status = control.make_query("Hospital_staff", 'public_id', f'{hospital.id}{user.id}')
                hospital.update(user_role=staff_status.user_role)
            return render_template('user/dashboard/dashboard.html', user=page, staff_invites=staff_invites)
    if page: # If the person requesting is not the owner of the page
        return "This page will display information of this user to people searching for them. Like how people can view your twitter profile"
    else: # If the user does not exist
        return "User does not Exist"
