from Blueprint.nurse import nurse
from flask import render_template, redirect, url_for, flash

@nurse.route('/dashboard')
def dashboard():
    assigned_patients = Patient.query.filter_by(nurse_id= current_user.id).all()
    upcoming_appointments = Appointment.query.filter_by(nurse_id= current_user.id).all()

    return render_template('nurse/dashboard.html', patients=assigned_patients, appointments=upcoming_appointments)

@nurse.route('/book', methods=['POST', 'GET'])
@login_required

def book():
    #Book a patient
    form = bookForm()

    if form.validate_on_submit():
        #check if doctor is avaliable at the chosen appointment time
        doctor = form.doctor.data
        appointment_time = form.appointment_time.data

        if is_doctor_available(doctor, appointment_time):
            #create the appointment
            appointment = Appointment(
                nurse_id = current_user.id,
                patient_id = form.patient.data.id,
                doctor = doctor.id,
                appointment_time = appointment_time
            )
            # Mark the doctor as unavailable at this appointment time
            mark_doctor_unavailable(doctor, appointment_time)

            #save the appointment and update the doctor's availability
            db.session.add(appointment)
            db.session.commit()
            flash('Appointment scheduled successfully', 'success')
            return redirect(url_for('nurse.dashboard'))
        else:
            flash('Selected doctor is not available at the chosen time')
    render_template('nurse/book.html', form=form)

    def is_doctor_available(doctor, appointment_time):
        exisitng_appointment = Appointment.query.filter_by(doctor_id=doctor.id, appointment_time=appointment_time).first()
        return exisitng_appointment is None
    def mark_doctor_available(doctor, appointment_time):
        doctor.availability.append(appointment_time)
        db.session.commit()