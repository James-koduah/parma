from blueprints.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user

@hospital.route('/accept_appointment/', methods=['post'], strict_slashes=False)
def hospital_accept_appointment():
    doctor = auth_user()
    if doctor == False:
        return redirect('/')
    
    check = control.check_current_appointments(doctor.public_id)
    if check:
        return jsonify({"response": "Cannot accept new appointment, You are already engaged"})
    message = request.get_json()
    appointment = message['appointment_id']
    appointment = control.make_query('Appointment', 'public_id', appointment)
    appointment.update(
            current_doctor_id=doctor.public_id,
            status='with_doctor'
            )
    control.commit_session()
    return jsonify({"response": "success"})

@hospital.route('/close_appointment/', methods=['post'], strict_slashes=False)
def hospital_close_appointment():
    doctor = auth_user()
    if doctor == False:
        return redirect('/')
    
    message = request.get_json()
    appointment = message['appointment_id']
    appointment = control.make_query('Appointment', 'public_id', appointment)
    appointment.update(
            status='closed'
            )
    control.commit_session()
    return jsonify({"response": "success"})

