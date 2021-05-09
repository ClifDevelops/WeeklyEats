from flask import Blueprint, jsonify, session, request
from app.models import Ingredient, Meal, UserMeal, db
from flask_login import login_required, current_user
from app.forms import MealForm

meal_routes = Blueprint('meals', __name__)

@meal_routes.route('/', methods=['POST'])
@login_required
def addToMeals():
    #add meal to Meal table
    userId = current_user.id
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
    #connect the meal and the current user on the userMeals table
        new_meal = Meal.query.filter(Meal.name == form.data['name']).first()
        new_meal_dict = new_meal.to_dict()
        user_meal = UserMeal(user_id=userId, meal_id=new_meal_dict['id'])
        db.session.add(user_meal)
        db.session.commit()
        return meal.to_dict()

    return 'Hello'

@meal_routes.route('/', methods=['GET'])
@login_required
def getMeals():
    #query for meal ids that a user has associated with their id
    userId = current_user.id
    userMealArr = UserMeal.query.filter(UserMeal.user_id == userId).all()
    userMealToDict = [user_meal.to_dict() for user_meal in userMealArr]
    mealIds = [meal['meal_id'] for meal in userMealToDict]
    #go through the meals table and add each meal to the array that we'll return to the thunk.
    mealsArray = []
    for mealId in mealIds:
        mealsArray.append(Meal.query.filter(Meal.id == mealId).first())
   
    mealsObj = [meal.to_dict() for meal in mealsArray]
    # print(mealsObj)
    return {'meals': mealsObj}
