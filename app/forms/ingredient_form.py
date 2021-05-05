from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Ingredient

class IngredientForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    type = StringField('type', validators=[DataRequired()])
    measurementUnit = StringField('measurementUnit', validators=[DataRequired()])
