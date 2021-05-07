from flask import Blueprint, jsonify, session, request
from app.models import Ingredient, db
from flask_login import login_required
from app.forms import IngredientForm

ingredient_routes = Blueprint('ingredients', __name__)

@ingredient_routes.route('/', methods=['POST'])
@login_required
def addToIngredients():
    
    form = IngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = Ingredient(
            name=form.data['name'],
            type=form.data['type'],
        )
        db.session.add(ingredient)
        db.session.commit()
        # print(ingredient)
        return ingredient.to_dict()
    return


@ingredient_routes.route('/', methods=['GET'])
@login_required
def getIngredients():
    ingredientsArray = Ingredient.query.all()
    ingredientsObj = [ingredient.to_dict() for ingredient in ingredientsArray]
    # print(ingredientsObj)
    return {'ingredients': ingredientsObj}
