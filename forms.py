from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length



class AddType(FlaskForm):
    name = StringField("Название тура")
    description  = IntegerField("Описание")
    sub = SubmitField("Добавить")