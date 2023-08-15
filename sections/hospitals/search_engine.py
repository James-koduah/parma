from sections.hospitals import hospitals
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control

@hospitals.route('/search', methods=['post'], strict_slashes=False)
def search_hospitals():
    search = request.get_json()['message']
    if search == '':
        all = control.get_all_hospitals()
    else:
        all = control.search_hospital('name', search)
    return jsonify({'hospitals': all})


@hospitals.route('/search_match', methods=['post'], strict_slashes=False)
def get_hospitals_match():
    search = request.get_json()['message']
    if search == '':
        jsonify({'matches': False})
    else:
        matches = control.get_hospital_matches('name', search)
    return jsonify({'matches': matches})
