from blueprints.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user

@hospital.route('/add_patient/', methods=['post'], strict_slashes=False)
def hospital_add_patient():
    user = auth_user()
    if user == False:
        return redirect('/login')
    message = request.get_json()
    name = message['patient_name']
    birth_date = message['birth_date']
    national_id = message['national_id']
    contact = message['contact']
    hospital_id = message['hospital_id']
    """national_id must be unique so check database if it already exists"""
    check = control.make_query('Patient', 'national_id', national_id)
    if check: 
        return jsonify({"status": 'error',"response": "National Id already exists"})
    """make public id"""
    while True:
        public_id = control.create_token(20)
        check = control.make_query('Patient', 'public_id', public_id)
        if check == None:
            break
    patient = control.evaluate('Patient')
    patient.update(
            public_id=public_id,
            name=name,
            birth_date=birth_date,
            national_id=national_id,
            contact=contact,
            hospital_id=hospital_id
            )

    control.add_item(patient)
    control.commit_session()
    return jsonify({"status": "success","response": patient.public_id})

@hospital.route('/search_patient', methods=['post'], strict_slashes=False)
def hospital_search_patient():
    user = auth_user()
    if user == False:
        return redirect('/')
    message = request.get_json()
    arg = message['search_string']
    patients = control.search_patients(arg)
    result = []
    for patient in patients:
        result.append(patient.to_dict())
    return jsonify({"response": result})


@hospital.route('/set_appointment', methods=['post'], strict_slashes=False)
def hospital_set_appointment():
    user =auth_user()
    if user == False:
        return redirect('/')
    message = request.get_json()
    hospital_id = message['hospitalId']
    patient_id = message['patientId']
    info = message['info']
    """Check if patient exists"""
    check = control.make_query('Patient', 'public_id', patient_id)
    if check == None:
        return jsonify({'response': "Wrong patient ID"})
    check = control.check_set_appointments(patient_id)
    if check:
        return jsonify({'response': "Patient is already open for attention"})
    """Generate public id"""
    while True:
        public_id = control.create_token(20)
        check = control.make_query('Appointment', 'public_id', public_id)
        if check == None:
            break
    appointment = control.evaluate('Appointment')
    appointment.update(
            public_id=public_id,
            hospital_id=hospital_id,
            patient_id=patient_id,
            info=info,
            status='open'
            )
    control.add_item(appointment)
    control.commit_session()
    return jsonify({"response": "Success"})
