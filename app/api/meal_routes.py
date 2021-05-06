from flask import Blueprint, jsonify, session, request
from app.models import Ingredient, Meal, db
from flask_login import login_required
from app.forms import MealForm

meal_routes = Blueprint('meals', __name__)

@meal_routes.route('/', methods=['POST'])
@login_required
def addToMeals():
    form = MealForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        meal = Meal(
            name=form.data['name'],
            cuisine=form.data['cuisine'],
            recipe=form.data['recipe']
        )
        db.session.add(meal)
        db.session.commit()
        return meal.to_dict()
    return 'Hello'