from sections.admin import admin
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control

@admin.route('/create_hospital', methods=['get', 'post'], strict_slashes=False)
def create_hospital():
    control.start_session()
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        about = request.form.get('about')
        hospital = control.evaluate('Hospital')
        if name == '' or location == '' or about == '':
            return redirect(request.referer)
        public_id = control.create_token(15)
        hospital.update(name=name, location=location, about=about, public_id=public_id)
        control.add_item(hospital)
        control.commit_session()
        return render_template(
                'confirmation.html',
                header='Request Received',
                content='Your submission has been sent to Headquaters for authorization, You will be contacted soon',
                action='You will be redirected in a few seconds'
                )
    else:
        return render_template('admin/create_hospital.html')
