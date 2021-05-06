from flask import Blueprint, jsonify, session, request
from app.models import Ingredient, Meal, UserMeal, db
from flask_login import login_required, current_user
from app.forms import MealForm

meal_routes = Blueprint('meals', __name__)

@meal_routes.route('/', methods=['POST'])
@login_required
def addToMeals():
    userId = current_user.id
    form = MealForm()
    # meal_name = form.data['name'] 
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        meal = Meal(
            name=form.data['name'],
            cuisine=form.data['cuisine'],
            recipe=form.data['recipe']
        )
        db.session.add(meal)
        db.session.commit()

        new_meal = Meal.query.filter(Meal.name == form.data['name']).first()
        new_meal_dict = new_meal.to_dict()
        # print('!!!!!!!!!!!!!!!!!!!!!!!', new_meal_dict)
        user_meal = UserMeal(user_id=userId, meal_id=new_meal_dict['id'])
        # print(user_meal)

        db.session.add(user_meal)
        db.session.commit()
        return meal.to_dict()

    return 'Hello'