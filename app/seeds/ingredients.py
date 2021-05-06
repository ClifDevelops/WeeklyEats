from app.models import db, Ingredient, MealIngredient

def seed_ingredients():
    ingredient1 = Ingredient(name='apples', type='fruit', measurementUnit='each')
    ingredient2 = Ingredient(
        name='oranges', type='fruit', measurementUnit='each')
    ingredient3 = Ingredient(
        name='bananas', type='fruit', measurementUnit='each')
    ingredient4 = Ingredient(
        name='blueberries', type='fruit', measurementUnit='each')
    ingredient5 = Ingredient(
        name='raspberries', type='fruit', measurementUnit='each')
    ingredient6 = Ingredient(
        name='coconuts', type='fruit', measurementUnit='each')
    ingredient7 = Ingredient(
        name='cantaloupes', type='fruit', measurementUnit='each')
    ingredient8 = Ingredient(
        name='cherries', type='fruit', measurementUnit='each')
    ingredient9 = Ingredient(
        name='blackberries', type='fruit', measurementUnit='each')
    
    db.session.add(ingredient1)
    db.session.add(ingredient2)
    db.session.add(ingredient3)
    db.session.add(ingredient4)
    db.session.add(ingredient5)
    db.session.add(ingredient6)
    db.session.add(ingredient7)
    db.session.add(ingredient8)
    db.session.add(ingredient9)
    

    db.session.commit()

def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
    

def seed_meal_ingredients():
    one = MealIngredient(meal_id=1, ingredient_id=1, ingredient_quantity=0.5)

    db.session.add(one)

    db.session.commit()


def undo_meal_ingredients():
    return
