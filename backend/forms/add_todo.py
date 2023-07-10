from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, DateTimeLocalField
from wtforms.validators import DataRequired, InputRequired

class AddTodoForm(FlaskForm):
    task_name = StringField('task_name', validators=[DataRequired()])
    task_time = DateTimeLocalField('datetime', validators=[InputRequired()])
    submit = SubmitField('Submit')