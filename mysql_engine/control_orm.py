from sqlalchemy import Column, Integer, String, UniqueConstraint, Date
from sqlalchemy import create_engine, delete, and_, or_
from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker
from mysql_engine.base import Base
from mysql_engine.hospital import Hospital
from mysql_engine.user import User
from mysql_engine.admin import Admin
from mysql_engine.junction_tables import Hospital_staff
from mysql_engine.invite_staff import Invite_staff
from mysql_engine.patient import Patient
from mysql_engine.drug import Drug
from mysql_engine.appointment import Appointment


class Control():
    """A class that provides an interface for easy usage of data from database"""
    engine = create_engine("mysql+mysqldb://parma:parma@localhost/parma")
    session = None

    def start_session(self):
            """Starts a session"""
            self.session = sessionmaker(bind=self.engine)()
            Base.metadata.create_all(bind=self.engine)

    def close_session(self):
        """Close session"""
        self.session.close()

    def commit_session(self):
        """Commit session"""
        try:
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            print('Cannot commit changes...Maybe:')
            print('there is nothing to commit')
            print('The item you are adding already exists')
            return None

    def add_item(self, new_item):
        """Add item"""
        if new_item:
            self.session.add(new_item)

    def delete_item(self, item):
        """Delete item"""
        if item:
            self.session.delete(item)

    def evaluate(self, table_name):
        """ Returns a new instance of an object
            This new instance represents a new row
            You can use the update functions in the instance to pass in new values
            Then add this row to session
        """
        instance = eval(table_name)
        return instance()

    def get_all_hospitals(self):
        objs = self.session.query(Hospital).all()
        objs_to_dict = []
        for obj in objs:
            item = obj.to_dict()
            objs_to_dict.append(item)
        return objs_to_dict

    def search_hospital(self, filter_by, arg):
        search = f'{arg}%'
        objs = self.session.query(Hospital).filter(Hospital.name.like(search)).all()
        objs_to_dict = []
        for obj in objs:
            item = obj.to_dict()
            objs_to_dict.append(item)
        return objs_to_dict

    def get_hospital_matches(self, filter_by, arg):
        search = f'{arg}%'
        objs = self.session.query(Hospital).filter(Hospital.name.like(search)).all()
        res = []
        for obj in objs:
            item = []
            item.append(obj.name)
            item.append(obj.location)
            res.append(item)
        return res


    def make_query(self, table_name, filter_by, arg):
        """Make a query"""
        table_name = eval(table_name)
        obj = None
        if filter_by == 'id':
            obj = self.session.query(table_name).filter_by(id=arg).first()
        if filter_by == 'username':
            obj = self.session.query(table_name).filter_by(username=arg).first()
        if filter_by == 'public_id':
            obj = self.session.query(table_name).filter_by(public_id=arg).first()
        if filter_by == 'email':
            obj = self.session.query(table_name).filter_by(email=arg).first()
        if filter_by == 'national_id':
            obj = self.session.query(table_name).filter_by(national_id=arg).first()
        return obj

    def check_admin_status(self, hospital_id, user_id):
        """Check if the user is an admin in a particular hospital"""
        obj = self.session.query(Admin).filter(and_(Admin.hospital_id==hospital_id, Admin.user_id==user_id)).first()
        return obj

    def get_staff_invite_user(self, user_id, status):
        """Get invites to a hospital of a user"""
        objs = self.session.query(Invite_staff).filter(and_(Invite_staff.user_id==user_id, Invite_staff.status==status)).all()
        return objs

    def get_staff_invite_hospital(self, hospital_id, status):
        """Get all Staff invites sent by a hospital"""
        objs = self.session.query(Invite_staff).filter(and_(Invite_staff.hospital_id==hospital_id, Invite_staff.status==status)).all()
        return objs

    def get_hospital_doctors(self, hospital_id):
        """Get all Staff invites sent by a hospital"""
        objs = self.session.query(Hospital_staff).filter(and_(Hospital_staff.hospital_id==hospital_id, Hospital_staff.user_role=='Doctor')).all()
        doctors=[]
        for obj in objs:
            doctor = self.make_query('User', 'id', obj.user_id)
            doctors.append(doctor)
        return doctors

    def get_appointments(self, hospital_id):
        """Get all appointments for a hospital"""
        objs = self.session.query(Appointment).filter(and_(Appointment.hospital_id==hospital_id, Appointment.status=='open')).all()
        for appointment in objs:
            patient = self.make_query('Patient', 'public_id', appointment.patient_id)
            appointment.update(patient_name=patient.name)
        return objs

    def check_current_appointments(self, doctor_id):
        obj = self.session.query(Appointment).filter(and_(Appointment.status=='with_doctor', Appointment.current_doctor_id==doctor_id)).first()
        if obj:
            patient = self.make_query('Patient', 'public_id', obj.patient_id)
            obj.update(patient_name=patient.name)
        return obj

    def check_set_appointments(self, patient_id):
        obj = self.session.query(Appointment).filter(and_(Appointment.status=='open', Appointment.patient_id==patient_id)).first()
        return obj

    def create_token(self, length):
        """Create a random token or password
           @length: length of token or password
        """
        import string
        import secrets
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password	

    def search_patients(self, arg):
        """search for a patient in the patients database"""
        objs=self.session.query(Patient).filter(or_(Patient.name==arg, Patient.national_id==arg, Patient.public_id==arg)).all()
        return objs
    

    def auth_token(self, token, username):
        user = self.make_query('User', 'username', username)
        if user:
            if user.login_token == token:
                return True
        return False

control = Control()
