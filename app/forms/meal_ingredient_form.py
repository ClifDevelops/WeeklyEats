from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import MealIngredient


class MealIngredientForm(FlaskForm):
    ingredient_id = IntegerField('ingredient_id', validators=[DataRequired()])
    # ingredient_quantity = IntegerField(
    #     'ingredient_quantity', validators=[DataRequired()])
    # measurement_unit = StringField(
    #     'measurement_unit', validators=[DataRequired()])
