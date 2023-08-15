from sections.hospitals import hospitals
from flask import Flask, render_template, request, redirect, jsonify
from __main__ import control

@hospitals.route('/', strict_slashes=False)
def main():
    control.start_session()
    return render_template('hospitals.html')
