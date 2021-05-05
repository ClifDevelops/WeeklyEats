from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, ValidationError
from app.models import Meal


class MealForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    cuisine = StringField('cuisine', validators=[DataRequired()])
    recipe = TextField('recipe', validators=[DataRequired()])
