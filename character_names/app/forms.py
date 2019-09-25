from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    descriptor = StringField('Descriptor', validators=[DataRequired()])
    
    submit = SubmitField('Submit')