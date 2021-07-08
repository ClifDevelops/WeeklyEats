from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Ingredient


def ingredient_exists(form, field):
    print("Checking if ingredient exists", field.data)
    ingredient_name = field.data
    ingredient = Ingredient.query.filter(Ingredient.name == ingredient_name).first()
    if ingredient:
        raise ValidationError("Ingredient is already on the list.")

class IngredientForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), ingredient_exists])
    type = StringField('type', validators=[DataRequired()])
    
