from flask import Blueprint, jsonify, session, request
from app.models import Ingredient, Meal, UserMeal, MealIngredient, db
from flask_login import login_required, current_user
from app.forms import MealForm, MealIngredientForm

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


@meal_routes.route('/edit', methods=['POST'])
@login_required
def editMeal():
    #add meal to Meal table
    form = MealForm()
    meal_id = request.json['meal_id']
    updated_meal = Meal.query.filter(Meal.id == meal_id).first()
    updated_meal.name = form.data['name']
    updated_meal.cuisine = form.data['cuisine']
    updated_meal.recipe = form.data['recipe']
    form['csrf_token'].data = request.cookies['csrf_token']
    db.session.commit()
    # if form.validate_on_submit():
    #     updated_meal = Meal(
    #         name=form.data['name'],
    #         cuisine=form.data['cuisine'],
    #         recipe=form.data['recipe']
    #     )
    #     db.session.add(updated_meal)
    #     db.session.commit()
    #     return updated_meal.to_dict()
    return updated_meal.to_dict()

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


@meal_routes.route('/ingredient', methods=['POST'])
@login_required
def addToMealIngredients():
    form = MealIngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print(request.json)
    meal_id = request.json['meal_id']
    print(meal_id)
    meal_ingredient = MealIngredient(
        meal_id= meal_id,
        ingredient_id=form.data['ingredient_id']
        # ingredient_quantity=form.data['ingredient_quantity'],
        # measurement_unit=form.data['measurement_unit']
    )
    db.session.add(meal_ingredient)
    db.session.commit()
    return meal_ingredient.to_dict()
