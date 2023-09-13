from  blueprints.nurse import nurse
from flask import render_template,request, redirect, session, url_for, flash
from __main__ import control
from mysql_engine.doctor import Doctor
import uuid
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from mysql_engine.appointment import Appointment

@nurse.route('/book', methods=['get', 'post'], strict_slashes=False)
def book_appointment():
    if request.method == 'POST':
        doctor = None
        try:
            patient_id = request.form['id']
            description = request.form['desc']
            doctor_id = request.form['doctor_id']  
            appointment_time = request.form['appointment_time']

            # Convert the appointment_time string to a datetime object
            appointment_time = datetime.strptime(appointment_time, '%H:%M')

            # Fetch the doctor's information based on the doctor_id
            doctor = control.make_query('Doctor', 'id', doctor_id)
            public_id = str(uuid.uuid4())
            hospital_id = 'jAvzDVFdUipE6nddiA5p'

            if doctor:
                # Create the appointment and associate it with the doctor
                appointment = Appointment(
                    public_id = public_id,
                    hospital_id = hospital_id,
                    patient_id=patient_id,
                    appointment_time=appointment_time,
                    doctor_id=doctor_id,
                    status=None,
                    description=description
                )

                # Add the appointment to your session and commit it to the database
                control.add_item(appointment)
                control.commit_session()

                flash('Successfully booked patient')
            else:
                flash('Doctor not found')

        except KeyError as e:
            flash(f'Missing form field: {str(e)}')
        except ValueError as e:
            flash(f'Invalid input: {str(e)}')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')

    return render_template('/hospital/staff/nurse.html')