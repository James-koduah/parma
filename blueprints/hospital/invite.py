from blueprints.hospital import hospital
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control, auth_user


@hospital.route('/<hospital_id>/invite', strict_slashes=False)
def hospital_invite(hospital_id):
    return 'james told you'
