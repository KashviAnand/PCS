from flask import Blueprint, render_template, request
from model import Student
from db import db

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/add', methods=['GET', 'POST'])
def add_student():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        student = Student(
            name=name,
            email=email,
            course=course
        )

        db.session.add(student)
        db.session.commit()

    return render_template('add_student.html')