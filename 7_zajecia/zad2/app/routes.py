from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Teacher
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/list')
def list_teachers():
    teachers = Teacher.query.all()
    return render_template('list_teachers.html', teachers=teachers)

@bp.route('/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        raw_time = request.form['time']

        if name and subject and raw_time:
            parsed_time = datetime.strptime(raw_time, '%H:%M').time()
            new_teacher = Teacher(name=name, subject=subject, time=parsed_time)
            db.session.add(new_teacher)
            db.session.commit()
            return redirect(url_for('main.list_teachers'))

    return render_template('add_teacher.html')

@bp.route('/delete/<int:teacher_id>', methods=['POST'])
def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for('main.list_teachers'))