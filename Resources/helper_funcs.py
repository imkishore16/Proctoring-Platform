from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, DateTimeField, BooleanField, IntegerField, DecimalField, HiddenField, SelectField, RadioField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField
from wtforms.validators import ValidationError, NumberRange
from datetime import timedelta, datetime


class UploadForm(FlaskForm):
    subject = StringField('Subject')
    topic = StringField('Topic')
    doc = FileField('CSV Upload', validators=[FileRequired()])
    start_date = DateField('Start Date')
    start_time = TimeField(
        'Start Time', default=datetime.utcnow()+timedelta(hours=5.5))
    end_date = DateField('End Date')
    end_time = TimeField(
        'End Time', default=datetime.utcnow()+timedelta(hours=5.5))
    calc = BooleanField('Enable Calculator')
    neg_mark = DecimalField('Enable negative marking in % ', validators=[
                            NumberRange(min=0, max=100)])
    duration = IntegerField('Duration(in min)')
    password = PasswordField(
        'Exam Password', [validators.Length(min=3, max=6)])
    proctor_type = RadioField('Proctoring Type', choices=[(
        '0', 'Automatic Monitoring'), ('1', 'Live Monitoring')])

    def validate_end_date(form, field):
        if field.data < form.start_date.data:
            raise ValidationError(
                "End date must not be earlier than start date.")

    def validate_end_time(form, field):
        start_date_time = datetime.strptime(str(form.start_date.data) + " " + str(
            form.start_time.data), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M")
        end_date_time = datetime.strptime(str(form.end_date.data) + " " + str(
            field.data), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M")
        if start_date_time >= end_date_time:
            raise ValidationError(
                "End date time must not be earlier/equal than start date time")

    def validate_start_date(form, field):
        if datetime.strptime(str(form.start_date.data) + " " + str(form.start_time.data), "%Y-%m-%d %H:%M:%S") < datetime.now():
            raise ValidationError(
                "Start date and time must not be earlier than current")


def examcreditscheck():
    # cur = mysql.connection.cursor()
    # results = cur.execute(
    #     'SELECT examcredits from users where examcredits >= 1 and email = %s and uid = %s', (session['email'], session['uid']))
    results=1
    if results > 0:
        return True