from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class OverrideForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[DataRequired()])
    course_name= StringField('Course Name', validators=[DataRequired()])
    course_number = StringField('Course Number', validators=[DataRequired()])
    course_instructor = StringField('Course Instructor', validators=[DataRequired()])
    reason = StringField('Reason for Override', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def override_request():
    student_name = None
    student_id = None
    course_name = None
    course_number = None
    course_instructor = None
    reason = None
    form = OverrideForm()
    if form.validate_on_submit():
        # Handle form submission, e.g., store data in the database
        flash('The course override has been submitted', 'success')
        return redirect(url_for('override_request'))
    return render_template('override_form.html', form=form, student_name=student_name, student_id=student_id, course_name=course_name, course_number=course_number, course_instructor=course_instructor, reason=reason)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
