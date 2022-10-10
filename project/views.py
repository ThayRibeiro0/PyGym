from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy.orm import Session
from . import db
from .models import Student

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    student = getstudent()
    return render_template("home.html", user=current_user, result=student, total=len(student))

#home
def getstudent():
    result = db.session.execute('SELECT * FROM student').fetchall()
    db.session.close()
    return result

@views.route('/', methods=['GET', 'POST'])
def cadastrar():
    fullname = request.form.get('fullname')
    birthdate = request.form.get('birthdate')
    address = request.form.get('address')
    cellphone = request.form.get('cellphone')
    course = request.form.get('course')
    payment = request.form.get('payment')

    new_student = Student(fullname=fullname, birthdate=birthdate, address=address, cellphone=cellphone, course=course, payment=payment)
    db.session.add(new_student)
    db.session.commit()
    db.session.close()
    return redirect(url_for('views.home'))

@views.route('/deletar/<id>')
def deletar(id: int):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route('/atualizar/<id>', methods=['GET', 'POST'])
def atualizar(id: int):
    if request.method == 'POST':
        new_student1 = {
            'id': id,
            'fullname': request.form.get('fullname'),
            'birthdate': request.form.get('birthdate'),
            'address': request.form.get('address'),
            'cellphone': request.form.get('cellphone'),
            'course': request.form.get('course'),
            'payment': request.form.get('payment')
        };

        db.session.execute("UPDATE student SET fullname = :fullname, birthdate = :birthdate, address = :address, cellphone = :cellphone, course = :course, payment = :payment WHERE id = :id", new_student1)
        db.session.commit()
        db.session.close()
        return redirect(url_for('views.home'))

    atualizar = getstudents(id)
    print(f"id {id}")
    return render_template('update.html', students=atualizar)

def getstudents(student_id: int):
    students = db.session.execute(f'SELECT * FROM student WHERE id = {student_id}').fetchone()
    db.session.close()
    return students

@views.route('/funcionarios')
def funcionarios():
    study = getstudy()
    return render_template('funcionarios.html', user=current_user, resulta=study, total=len(study))

def getstudy():
    resulta = db.session.execute('SELECT * FROM user').fetchall()
    db.session.close()
    return resulta